import pytest
from flask import Flask
from lib.applications import ApplicationError, Route, Application, CustomApplication, Todo, TodoSetup

_module_runner: str = "__main__"


@pytest.fixture(scope="module")
def custom() -> Application:
    return CustomApplication(_module_runner, static_folder="static", template_folder="templates")


@pytest.fixture(scope="module")
def todo() -> Application:
    return Todo(_module_runner)


@pytest.fixture(scope="module")
def setup() -> TodoSetup:
    return TodoSetup()


@pytest.mark.parametrize("route, result", [("root", "/"), ("home", "index.html")])
def test_route_from_str(route: str, result: str) -> None:
    assert Route.from_str(route) == result


def test_wrong_route_from_str() -> None:
    with pytest.raises(ApplicationError):
        Route.from_str("N/A")


def test_str_route() -> None:
    assert str(Route.ROOT) == "/"


def test_custom_engine(custom: Application) -> None:
    assert isinstance(custom.engine, Flask)


def test_todo_engine(todo: Application) -> None:
    assert isinstance(todo.engine, Flask)


def test_todo_setup_module(setup: TodoSetup) -> None:
    assert setup.module == _module_runner


def test_todo_setup_database(setup: TodoSetup) -> None:
    assert setup.database == "sqlite:///todo.db"
