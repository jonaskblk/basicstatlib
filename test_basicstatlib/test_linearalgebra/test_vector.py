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
    assert vector.get_components.__eq__(values)

def test___eq__() -> None:
    vector_a = Vector([5, 7, 9])
    vector_b = Vector([5, 7, 9])
    vector_c = Vector([2, 3, 5])
    assert vector_a.__eq__(vector_b)
    assert not vector_a.__eq__(vector_c)

def test___str__() -> None:
    vector = Vector([5, 7, 9])
    str_of_vector = "[5, 7, 9]"
    assert vector.__str__().__eq__(str_of_vector)

def test___repr__() -> None:
    vector = Vector([5, 7, 9])
    repr_of_vector = "Vector([5, 7, 9])"
    assert vector.__repr__().__eq__(repr_of_vector)

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
    assert vector.get_components.__eq__(values)

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

@pytest.mark.parametrize("values", [
    (
        [1, 2, 3]
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
def test_get_component_by_index(values) -> None:
    vector_a = Vector(values)
    assert vector_a.get_component_by_index(1) == values[0]
    assert vector_a.get_component_by_index(2) == values[1]
    assert vector_a.get_component_by_index(3) == values[2]

def test_set_value_of_component() -> None:
    vector_a = Vector([1.0, 2.0, 3.0])
    index_of_component = 2
    new_value = 3.0
    vector_a.set_value_of_component(index_of_component, new_value)
    assert vector_a.get_component_by_index(index_of_component) == new_value

def test_add_two_vectors_success() -> None:
    vector_a = Vector([1, 2, 3])
    vector_b = Vector([4, 5, 6])
    vector_c = Vector([5, 7, 9])
    vector_a.add(vector_b)
    assert vector_a.__eq__(vector_c)

def test_subtract_two_vectors_success() -> None:
    vector_a = Vector([5, 7, 9])
    vector_b = Vector([1, 2, 3])
    vector_c = Vector([4, 5, 6])
    vector_a.subtract(vector_b)
    assert vector_a.__eq__(vector_c)

def test_multiply_with_scalar_success() -> None:
    vector_a = Vector([5, 7, 9])
    vector_b = Vector([10, 14, 18])
    scalar = 2
    vector_a.multiply_with_scalar(scalar)
    assert vector_a.__eq__(vector_b)