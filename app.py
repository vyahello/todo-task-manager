from abc import ABC, abstractmethod
from flask import Flask, render_template


class Application(ABC):
    """The class represents an abstract application."""

    root: str = "/"
    index: str = "index.html"

    @classmethod
    @abstractmethod
    def web_engine(cls) -> Flask:
        """Returns web engine of an application"""
        pass


def _run_todo_task_manager():
    """Runs `to-do` task manager application"""

    class Todo(Application):
        """The class represents """

        @classmethod
        def web_engine(cls) -> Flask:
            return Flask(__name__)

    engine: Flask = Todo.web_engine()

    @engine.route(Application.root)
    def index():
        """Returns an index page of an application."""
        return render_template(Application.index)

    engine.run()


if __name__ == "__main__":
    _run_todo_task_manager()
