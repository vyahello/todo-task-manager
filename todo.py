"""A module provides entrypoint API to run `to-do` task master application."""
from lib import master


def _run_master_application() -> None:
    """Runs `to-do` task master application."""
    master.run(host="0.0.0.0", port=7777)


if __name__ == "__main__":
    _run_master_application()
