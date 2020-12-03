import pytest
from flask import Flask
from lib.applications import (
    _APP_DIR,
    ApplicationError,
    Route,
    Application,
    CustomApplication,
    Todo,
    TodoRequest,
)


@pytest.fixture(scope="module")
def setup() -> TodoRequest:
    return TodoRequest()


@pytest.fixture(scope="module")
def custom(setup: TodoRequest) -> Application:
    return CustomApplication(setup.module, setup.database)


@pytest.fixture(scope="module")
def todo(setup: TodoRequest) -> Application:
    return Todo(setup)


@pytest.mark.parametrize(
    "route, result",
    [
        ("root", "/"),
        ("home_page", "/index.html"),
        ("delete_id", "/delete/<int:identity>"),
        ("update_id", "/update/<int:identity>"),
        ("update_page", "/update.html"),
    ],
)
def test_route_from_str(route: str, result: str) -> None:
    assert Route.from_str(route) == result


def test_wrong_route_from_str() -> None:
    with pytest.raises(ApplicationError):
        Route.from_str("N/A")


def test_allowed_routes() -> None:
    assert len(Route.allowed()) == 5


def test_wrong_route() -> None:
    with pytest.raises(KeyError):
        Route.allowed()["N/A"]


def test_str_route() -> None:
    assert str(Route.ROOT) == "/"


def test_call_custom(custom: Application) -> None:
    assert isinstance(custom(), Flask)


def test_call_todo(todo: Application) -> None:
    assert isinstance(todo(), Flask)


def test_todo_setup_module(setup: TodoRequest) -> None:
    assert setup.module == "__main__"


def test_todo_setup_database(setup: TodoRequest) -> None:
    assert setup.database == f"sqlite:///{_APP_DIR}/todo.db"


def test_todo_setup_static(setup: TodoRequest) -> None:
    assert setup.static_dir == f"{_APP_DIR}/static"


def test_todo_setup_templates(setup: TodoRequest) -> None:
    assert setup.template_dir == f"{_APP_DIR}/templates"
