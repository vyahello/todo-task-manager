import pytest
from lib.web.api import ApiMethod


def test_number_of_methods() -> None:
    assert len(ApiMethod)


def test_index_methods_number() -> None:
    assert len(ApiMethod.index()) == 2


@pytest.mark.parametrize(
    "value, result",
    [
        (ApiMethod.POST.value, "POST"),
        (ApiMethod.GET.value, "GET"),
        (ApiMethod.PUT.value, "PUT"),
        (ApiMethod.DELETE.value, "DELETE"),
    ],
)
def test_method(value: str, result: str) -> None:
    assert value == result
