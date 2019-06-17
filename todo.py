"""A module provides entrypoint API to run `to-do` task manager application."""
from flask import render_template
from lib.web.api import ApiMethod
from lib.applications import TodoSetup, Route, Application, Todo

todo: Application = Todo(str(TodoSetup.module))


def _run_todo_task_manager() -> None:
    """Runs `to-do` task manager application."""
    todo.config(str(TodoSetup.database))

    @todo.engine.route(Route.from_str("root"), methods=ApiMethod.index())
    def index():  # pylint: disable=unused-variable
        """Returns an index page of an application."""
        return render_template(Route.from_str("home"))

    todo.run(host="0.0.0.0", port=7777)


if __name__ == "__main__":
    _run_todo_task_manager()
