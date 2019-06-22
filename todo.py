"""A module provides entrypoint API to run `to-do` task manager application."""
from lib import main


if __name__ == "__main__":
    main.run(host="0.0.0.0", port=7777, debug=True)
