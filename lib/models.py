"""A module contains a set of API to work with database model."""
from datetime import datetime
from lib import database


class Content(database.model):  # type: ignore
    """The class represents database content model."""

    identity = database.column(database.type().integer, primary_key=True)
    content = database.column(database.type().string(length=200), nullable=False)
    date_created = database.column(database.type().datetime, default=datetime.utcnow)

    def __repr__(self):
        """Returns string representation."""
        return f"<Task {self.identity!r}>"
