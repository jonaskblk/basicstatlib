import pytest

from .. linearalgebra.vector import Vector

@pytest.mark.parametrize('values', [
    (
        [0, 1 ,3]
    ),
    (
        [0, 0, 0]
    ),
    (
        [-1, -2, -3]
    ),
    (
        [-1, 2, 33]
    ),
])
def test_create_int_vector_success(values) -> None:
    vector = Vector(values)
    assert vector.components.__eq__(values)

def test_create_float_vector_success() -> None:
    values = [1.1, 1.1, 3.0]
    vector = Vector(values)
    assert vector.components.__eq__(values)

def test_create_string_vector_fail() -> None:
    with pytest.raises(Exception):
        values = ["word", 1 ,3]
        Vector(values)

def test_create_empty_vector_fail() -> None:
    with pytest.raises(Exception):
        values = []
        Vector(values)

def test_add_two_vectors_success() -> None:
    vector_a = Vector([1, 2, 3])
    vector_b = Vector([4, 5, 6])
    vector_c = Vector([5, 7, 9])
    vector_a.add(vector_b)
    assert vector_a.components.__eq__(vector_c.components)