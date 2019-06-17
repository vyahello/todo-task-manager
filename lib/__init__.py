from lib.applications import Application, Todo, TodoRequest
from lib.databases import Database

todo_app: Application = Todo(TodoRequest())
todo_app.setup()
database = Database(todo_app)
