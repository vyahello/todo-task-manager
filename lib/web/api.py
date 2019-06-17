"""A module contains API for web requests."""
from enum import Enum
from typing import Tuple


class ApiMethod(Enum):
    """Represents api web methods."""

    POST: str = "POST"
    GET: str = "GET"
    PUT: str = "PUT"
    DELETE: str = "DELETE"

    @classmethod
    def index(cls) -> Tuple[str, ...]:
        """Index page methods."""
        return cls.POST.value, cls.GET.value

    def __len__(self) -> int:
        """Returns number of api requests."""
        return len(self)
