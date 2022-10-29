import pytest
from qlib.math.vector import Vector, VectorValidator


class TestVector:

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
    def test_create_int_vector_success(self, values) -> None:
        vector = Vector(values)
        assert vector.get_components() == values

    def test___eq__(self) -> None:
        vector_a = Vector([5, 7, 9])
        vector_b = Vector([5, 7, 9])
        vector_c = Vector([2, 3, 5])
        assert vector_a == vector_b
        assert vector_a != vector_c

    def test___str__(self) -> None:
        vector = Vector([5, 7, 9])
        str_of_vector = "[5.0, 7.0, 9.0]"
        assert vector.__str__() == str_of_vector

    def test___repr__(self) -> None:
        vector = Vector([5, 7, 9])
        repr_of_vector = "Vector([5.0, 7.0, 9.0])"
        assert vector.__repr__() == repr_of_vector

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
    def test_create_float_vector_success(self, values) -> None:
        """Checks, if the initilization of a vector object succeds, when the passed values are valid.
        """
        vector = Vector(values)
        assert vector.get_components() == values

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
    def test_create_string_vector_fail(self, values) -> None:
        """Checks, if the initilization of a vector object fails, when the passed values are not valid.
        """
        with pytest.raises(Exception):
            Vector(values)

    def test_create_empty_vector_fail(self) -> None:
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
    def test_get_component_by_index(self, values) -> None:
        vector_a = Vector(values)
        assert vector_a.get_component_by_index(1) == values[0]
        assert vector_a.get_component_by_index(2) == values[1]
        assert vector_a.get_component_by_index(3) == values[2]

    def test_set_value_of_component(self) -> None:
        vector_a = Vector([1.0, 2.0, 3.0])
        index_of_component = 2
        new_value = 3.0
        vector_a.set_value_of_component(index_of_component, new_value)
        assert vector_a.get_component_by_index(index_of_component) == new_value

    def test_add_two_vectors_success(self) -> None:
        vector_a = Vector([1, 2, 3])
        vector_b = Vector([4, 5, 6])
        vector_c = Vector([5, 7, 9])
        vector_a.add(vector_b)
        assert vector_a == vector_c

    def test_subtract_two_vectors_success(self) -> None:
        vector_a = Vector([5, 7, 9])
        vector_b = Vector([1, 2, 3])
        vector_c = Vector([4, 5, 6])
        vector_a.subtract(vector_b)
        assert vector_a == vector_c

    def test_multiply_with_scalar_success(self) -> None:
        vector_a = Vector([5, 7, 9])
        vector_b = Vector([10, 14, 18])
        scalar = 2
        vector_a.multiply_with_scalar(scalar)
        assert vector_a == vector_b

    def test_dot_product_success(self):
        pass

    def test_sum_of_squares(self):
        pass

    def test_magnitude(self):
        pass

    def test_distance_to(self):
        pass

    def test_sum_up_vectors(self):
        pass

    def test_mean_of_vectors(self):
        pass


class TestVectorValidator:

    def test_guard_components_not_empty(self) -> None:
        vector_validator = VectorValidator()
        vector_validator.guard_components_not_empty([1, 2, 3])

    def test_guard_components_of_type_float_or_int(self) -> None:
        pass

    def test_guard_is_of_type_vector(self) -> None:
        pass

    def test_guard_index_greater_then_zero(self) -> None:
        pass

    def test_guard_equal_length_of_components(self) -> None:
        pass

    def test_guard_equal_length_of_components_in_list(self) -> None:
        pass

    def test_guard_is_a_number(self) -> None:
        pass

    def test_guard_list_of_vectors_not_empty(self) -> None:
        pass
