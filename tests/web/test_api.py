import pytest
from lib.web.api import HttpMethod


def test_number_of_methods() -> None:
    assert len(HttpMethod)


def test_index_methods_number() -> None:
    assert len(HttpMethod.for_index()) == 2


def test_delete_methods_number() -> None:
    assert len(HttpMethod.for_update()) == 2


@pytest.mark.parametrize(
    "value, result",
    [
        (HttpMethod.POST.value, "POST"),
        (HttpMethod.GET.value, "GET"),
        (HttpMethod.PUT.value, "PUT"),
        (HttpMethod.DELETE.value, "DELETE"),
    ],
)
def test_method(value: str, result: str) -> None:
    assert value == result
