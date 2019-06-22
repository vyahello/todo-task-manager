"""A module provides entrypoint API to run `to-do` task manager application."""
from lib import todo_app


if __name__ == "__main__":
    todo_app.run(host="0.0.0.0", port=7777)
