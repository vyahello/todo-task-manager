"""A module contains a set of application routes."""
from typing import Union

from flask import request, redirect, render_template
from werkzeug.wrappers import Response
from flask_sqlalchemy.query import Query
from lib import master, database
from lib.applications import Route
from lib.models import Content
from lib.web.api import HttpMethod


@master.route(Route.from_str("home_page"))
@master.route(Route.from_str("root"), methods=HttpMethod.for_index())
def index():
    """Returns an index page of an application."""
    if request.method == HttpMethod.POST.value:
        database.add_session(Content(content=request.form["content"]))
        database.commit_session()
        return redirect(Route.from_str("root"))
    return render_template(
        Route.from_str("home_page"),
        tasks=Content.query.order_by(Content.date_created).all(),
    )


@master.route(Route.from_str("delete_id"))
def delete(identity: int) -> Response:
    """Deletes a task from task manager."""
    database.delete_session(Content.query.get_or_404(identity))
    database.commit_session()
    return redirect(Route.from_str("root"))


@master.route(Route.from_str("update_id"), methods=HttpMethod.for_update())
def update(identity: int) -> Union[str, Response]:
    """Updates a task."""
    task: Query = Content.query.get_or_404(identity)
    if request.method == "POST":
        task.content = request.form["content"]  # type: ignore
        database.commit_session()
        return redirect(Route.from_str("root"))
    return render_template(
        Route.from_str("update_page"), task=Content.query.get_or_404(identity)
    )
