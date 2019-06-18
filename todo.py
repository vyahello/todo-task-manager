"""A module provides entrypoint API to run `to-do` task manager application."""
# pylint: disable=unused-variable
from flask import render_template, request, redirect
from lib import todo_app, database
from lib.applications import Route
from lib.models import Content
from lib.web.api import ApiMethod


def _run_todo_task_manager() -> None:  # noqa: D202
    """Runs `to-do` task manager application."""

    @todo_app.engine.route(Route.from_str("root"), methods=ApiMethod.index())
    def index():
        """Returns an index page of an application."""
        if request.method == ApiMethod.POST.value:
            database.add_session(Content(content=request.form["content"]))
            database.commit_session()
            return redirect(Route.from_str("root"))
        return render_template(Route.from_str("home"), tasks=Content.query.order_by(Content.date_created).all())

    @todo_app.engine.route(Route.from_str("delete"))
    def delete(identity: int) -> None:
        """Deletes a task from task manager."""
        database.delete_session(Content.query.get_or_404(identity))
        database.commit_session()
        return redirect(Route.from_str("root"))

    todo_app.run()


if __name__ == "__main__":
    _run_todo_task_manager()
