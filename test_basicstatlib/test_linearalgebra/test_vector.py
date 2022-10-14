import pytest
from basicstatlib.linearalgebra.vector import Vector

@pytest.mark.parametrize("values", [
    (
        [0, 1, 3]
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

@pytest.mark.parametrize("values", [
    (
        [0.1, 1.0, 3.0]
    ),
    (
        [0.0, 0.0, 0.0]
    ),
    (
        [-1.0, -2.0, -3.0]
    ),
    (
        [-1.1, 2.0, 33.3]
    ),
])
def test_create_float_vector_success(values) -> None:
    vector = Vector(values)
    assert vector.components.__eq__(values)

@pytest.mark.parametrize("values", [
    (
        ["word", 1, 3]
    ),
    (
        [0.0, "word", 0.0]
    ),
    (
        ["test", "123", "word"]
    ),
])
def test_create_string_vector_fail(values) -> None:
    with pytest.raises(Exception):
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

def test_subtract_two_vectors_success() -> None:
    vector_a = Vector([5, 7, 9])
    vector_b = Vector([1, 2, 3])
    vector_c = Vector([4, 5, 6])
    vector_a.subtract(vector_b)
    assert vector_a.components.__eq__(vector_c.components)