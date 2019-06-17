"""A module contains a set of API to work with database model."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from todo import todo

database: SQLAlchemy = SQLAlchemy(todo.engine)


class TodoDatabase(database.Model):
    """The class represents database model."""

    identity: database.Column = database.Column(database.Integer, primary_key=True)
    content: database.Column = database.Column(database.String(length=200), nullable=False)
    completed: database.Column = database.Column(database.Integer, default=0)
    date_created: database.Column = database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        """Returns string representation."""
        return f"<Task {self.identity!r}>"
