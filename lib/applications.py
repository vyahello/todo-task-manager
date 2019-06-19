"""A module provides API to work with applications."""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, NamedTuple, Dict
from flask import Flask


class ApplicationError(Exception):
    """Raises error occurred in an application."""

    pass


class TodoRequest(NamedTuple):
    """The class represents setup for `to-do` application."""

    module: str = "__main__"
    database: str = "sqlite:///todo.db"


class Route(Enum):
    """The class represents route element."""

    ROOT: str = "/"
    HOME_PAGE: str = "/index.html"
    DELETE_ID: str = "/delete/<int:identity>"
    UPDATE_ID: str = "/update/<int:identity>"
    UPDATE_PAGE: str = "/update.html"

    @classmethod
    def from_str(cls, route: str) -> str:
        """Returns route from a string."""
        if route not in cls.allowed():
            raise ApplicationError(f'Given "{route}" route is invalid!')
        return str(cls.allowed()[route])

    @classmethod
    def allowed(cls) -> Dict[str, "Route"]:
        """Returns allowed routes mapping."""
        return {
            "root": cls.ROOT,
            "home_page": cls.HOME_PAGE,
            "delete_id": cls.DELETE_ID,
            "update_id": cls.UPDATE_ID,
            "update_page": cls.UPDATE_PAGE,
        }

    def __str__(self) -> str:
        """Returns string route value."""
        return self.value


class Application(ABC):
    """The class represents an abstract application."""

    @property
    @abstractmethod
    def engine(self) -> Flask:
        """Returns web engine of an application."""
        pass

    @abstractmethod
    def run(self, host: str, port: int, debug: bool = False, load_dot_env: bool = True, **options: Any) -> None:
        """Runs an application."""
        pass

    @abstractmethod
    def setup(self) -> None:
        """Setups an application config."""
        pass


class CustomApplication(Application):
    """The class represents a custom application."""

    def __init__(self, module: str, database: str, static_dir: str = "static", template_dir: str = "templates") -> None:
        self._engine: Flask = Flask(import_name=module, static_folder=static_dir, template_folder=template_dir)
        self._database: str = database

    @property
    def engine(self) -> Flask:
        """Returns web engine of a custom application."""
        return self._engine

    def run(self, host: str, port: int, debug: bool = False, load_dot_env: bool = True, **options: Any) -> None:
        """Runs a custom application."""
        return self._engine.run(host, port, debug, load_dot_env, **options)

    def setup(self) -> None:
        """Setups a custom application config."""
        self._engine.config["SQLALCHEMY_DATABASE_URI"] = self._database


class Todo(Application):
    """The class represents a `to-do` application."""

    def __init__(self, setup: TodoRequest) -> None:
        self._application: Application = CustomApplication(setup.module, setup.database)

    @property
    def engine(self) -> Flask:
        """Returns web engine of a `to-do` application."""
        return self._application.engine

    def run(self, host: str, port: int, debug: bool = False, load_dot_env: bool = True, **options: Any) -> None:
        """Runs a `to-do` application."""
        self._application.run(host, port, debug, load_dot_env, **options)

    def setup(self) -> None:
        """Setup a `to-do` application config."""
        self._application.setup()
