import pytest

from vectors import *

@pytest.mark.parametrize('vector_a, vector_b, expected', [
    (
        [1, 2, 3], [4, 5, 6], [5, 7, 9]
    ),
    (
        [0, 0, 0], [0, 0, 0], [0, 0, 0]
    ),
])
def test_add(vector_a, vector_b, expected):
    assert add(vector_a, vector_b) == expected

@pytest.mark.parametrize('vector_a, vector_b', [
    (
        [1, 2, 0], [3, 0]
    ),
])
def test_add_should_raise_exception(vector_a, vector_b):
    with pytest.raises(Exception):
        add(vector_a, vector_b)