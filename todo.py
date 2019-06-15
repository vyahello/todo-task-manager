"""This module provide entrypoint API to run `to-do` task manager application."""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any
from flask import Flask, render_template


class ApplicationError(Exception):
    """Raises error occurred in an application."""

    pass


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
        """Returns web engine of an application"""
        pass

    @abstractmethod
    def run(self, host: str, port: str, debug: bool = False, load_dot_env: bool = True, **options: Any) -> None:
        """Runs an application."""
        pass


class CustomApplication(Application):
    """The class represents a custom application."""

    def __init__(self, name: str) -> None:
        self._engine: Flask = Flask(name)

    @property
    def engine(self) -> Flask:
        return self._engine

    def run(self, host: str, port: str, debug: bool = False, load_dot_env: bool = True, **options: Any) -> None:
        self._engine.run(host, port, debug, load_dot_env, **options)


class Todo(Application):
    """The class represents a `to-do` application."""

    def __init__(self) -> None:
        self._application: Application = CustomApplication(__name__)

    @property
    def engine(self) -> Flask:
        return self._application.engine

    def run(self, host: str, port: str, debug: bool = False, load_dot_env: bool = True, **options: Any) -> None:
        self._application.run(host, port, debug, load_dot_env, **options)


def _run_todo_task_manager() -> None:
    """Runs `to-do` task manager application"""
    todo: Application = Todo()

    @todo.engine.route(Route.from_str("root"))
    def index():
        """Returns an index page of an application."""
        return render_template(Route.from_str("home"))

    todo.run(host="0.0.0.0", port="7777")


if __name__ == "__main__":
    _run_todo_task_manager()
