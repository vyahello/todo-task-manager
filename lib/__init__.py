from lib.applications import Application, Todo, TodoRequest
from lib.databases import Database

todo_app: Application = Todo(TodoRequest())
todo_app.setup()
database = Database(todo_app)
master = todo_app()

from lib import routes  # noqa: F401
