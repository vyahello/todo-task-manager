"""A module provides API to work with applications."""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, NamedTuple
from flask import Flask


class ApplicationError(Exception):
    """Raises error occurred in an application."""

    pass


class TodoSetup(NamedTuple):
    """The class represents setup for `to-do` application."""

    module: str = "__main__"
    database: str = "sqlite:///todo.db"


class Route(Enum):
    """The class represents route element."""

    ROOT: str = "/"
    HOME: str = "index.html"

    @classmethod
    def from_str(cls, route: str) -> str:
        """Returns route from a string."""
        if route == "root":
            return str(cls.ROOT)
        if route == "home":
            return str(cls.HOME.value)
        raise ApplicationError(f'Given "{route}" route is invalid!')

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
    def config(self, database_name: str) -> None:
        """Setup an application config."""
        pass


class CustomApplication(Application):
    """The class represents a custom application."""

    def __init__(self, name: str, static_folder: str, template_folder: str) -> None:
        self._engine: Flask = Flask(import_name=name, static_folder=static_folder, template_folder=template_folder)

    @property
    def engine(self) -> Flask:
        """Returns web engine of a custom application."""
        return self._engine

    def run(self, host: str, port: int, debug: bool = False, load_dot_env: bool = True, **options: Any) -> None:
        """Runs a custom application."""
        self._engine.run(host, port, debug, load_dot_env, **options)

    def config(self, database_name: str) -> None:
        """Setup a custom application config."""
        self._engine.config["SQLALCHEMY_DATABASE_URI"] = database_name


class Todo(Application):
    """The class represents a `to-do` application."""

    def __init__(self, name: str) -> None:
        self._application: Application = CustomApplication(name, static_folder="static", template_folder="templates")

    @property
    def engine(self) -> Flask:
        """Returns web engine of a `to-do` application."""
        return self._application.engine

    def run(self, host: str, port: int, debug: bool = False, load_dot_env: bool = True, **options: Any) -> None:
        """Runs a `to-do` application."""
        self._application.run(host, port, debug, load_dot_env, **options)

    def config(self, database_name: str) -> None:
        """Setup a `to-do` application config."""
        self._application.config(database_name)
