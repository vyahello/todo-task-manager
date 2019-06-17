"""A module provides API to work with databases."""
from typing import Type
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, Integer, String, DateTime
from lib import Application


class _ValueType:
    """Represents database type."""

    def __init__(self, database: SQLAlchemy) -> None:
        self._database: SQLAlchemy = database

    @property
    def integer(self) -> Type[Integer]:
        """Returns an integer type."""
        return self._database.Integer

    @property
    def string(self) -> Type[String]:
        """Returns a string type."""
        return self._database.String

    @property
    def datetime(self) -> Type[DateTime]:
        """Returns a datetime type."""
        return self._database.DateTime


class Database:
    """Represents a database."""

    def __init__(self, application: Application) -> None:
        self._db: SQLAlchemy = SQLAlchemy(application.engine)
        self._type: _ValueType = _ValueType(self._db)

    @property
    def model(self) -> Model:
        """Returns a datetime model."""
        return self._db.Model

    @property
    def column(self) -> Type[Column]:
        """Returns a datetime column."""
        return self._db.Column

    def type(self) -> _ValueType:
        """Returns a datetime datatype."""
        return self._type

    def add_session(self, model: Model):
        """Adds new session."""
        self._db.session.add(model)

    def commit_session(self):
        """Commits a session."""
        self._db.session.commit()
