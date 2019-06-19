"""A module contains API for web requests."""
from enum import Enum
from typing import Tuple


class HttpMethod(Enum):
    """Represents api web methods."""

    POST: str = "POST"
    GET: str = "GET"
    PUT: str = "PUT"
    DELETE: str = "DELETE"

    @classmethod
    def for_index(cls) -> Tuple[str, ...]:
        """Index page methods."""
        return cls.POST.value, cls.GET.value

    @classmethod
    def for_update(cls) -> Tuple[str, ...]:
        """Update option methods."""
        return cls.POST.value, cls.GET.value

    def __len__(self) -> int:
        """Returns number of api requests."""
        return len(self)
