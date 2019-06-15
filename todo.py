"""This module provides entrypoint API to run `to-do` task manager application."""
from flask import render_template
from lib.applications import Route, Application, Todo


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
