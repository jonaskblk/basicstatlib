import pytest

from .. linearalgebra.vector import Vector

def test_create_int_vector_success() -> None:
    values = [0, 1 ,3]
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
