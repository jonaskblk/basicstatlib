"""Contains all types and procedures associated with a mathematical vector.
"""

from .common import CommonValidator


class Vector:
    """Defines objects of type vector.

    Raises:
        Exception: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        Exception: _description_
        ValueError: _description_

    Returns:
        _type_: vector
    """

    def __init__(self, components: list) -> None:
        self.__vector_validator = VectorValidator()
        self.__vector_validator.guard_components_not_empty(components)
        self.__vector_validator.guard_components_of_type_float_or_int(
            components)

        self.__components = components

    def __eq__(self, other: 'object') -> bool:
        self.__vector_validator.guard_is_of_type_vector(other)

        return self.__components.__eq__(other.get_components())  # type: ignore

    def __str__(self) -> str:
        return self.__components.__str__()

    def __repr__(self) -> str:
        return f"Vector({self.__components.__str__()})"

    def get_components(self) -> list:
        """Returns the components of a vector object as a list.
        """
        return self.__components

    def get_component_by_index(self, index: int) -> float:
        self.__vector_validator.guard_index_greater_then_zero(index)

        return self.__components[index - 1]

    def set_value_of_component(self, index: int, value: float) -> float:  # type: ignore
        self.__vector_validator.guard_index_greater_then_zero(index)

        self.__components[index - 1] = value

    def add(self, vector_b: 'Vector'):
        vector_a = Vector(self.__components)
        self.__vector_validator.guard_equal_length_of_components(
            vector_a, vector_b)
        self.__components = [
            a_i + b_i for a_i, b_i in zip(vector_a.get_components(), vector_b.get_components())]

    def subtract(self, vector_b: 'Vector'):
        vector_a = Vector(self.__components)
        self.__vector_validator.guard_equal_length_of_components(
            vector_a, vector_b)
        self.__components = [
            a_i - b_i for a_i, b_i in zip(vector_a.get_components(), vector_b.get_components())]

    def multiply_with_scalar(self, scalar: float) -> None:
        self.__vector_validator.guard_is_a_number(scalar)
        vector = Vector(self.__components)
        self.__components = [
            index * scalar for index in vector.get_components()]

    def sum_of_squares(self) -> float:  # type: ignore
        pass

    def magnitude(self) -> float:  # type: ignore
        pass

    def distance(self, vector_b: 'Vector') -> float:  # type: ignore
        pass

    def squared_distance(self, vector_b: 'Vector') -> float:  # type: ignore
        pass

    @ staticmethod
    def sum_up_vectors(vectors: list['Vector']) -> 'Vector':  # type: ignore
        pass

    @ staticmethod
    def mean_of_vectors(vectors: list['Vector']) -> 'Vector':  # type: ignore
        pass


class VectorValidator:
    def __init__(self) -> None:
        self.common_validator = CommonValidator()

    def guard_components_not_empty(self, components: list) -> None:
        if (components == []):
            raise Exception("A Vector consists of at least one component")

    def guard_components_of_type_float_or_int(self, components: list) -> None:
        if (all([isinstance(component, float) for component in components])):
            pass
        elif (all([isinstance(component, int) for component in components])):
            pass
        else:
            raise ValueError("Components must be of type float or int")

    def guard_is_of_type_vector(self, object_to_check: object) -> None:
        if not (isinstance(object_to_check, Vector)):
            raise ValueError("Object must be of type vector")

    def guard_index_greater_then_zero(self, index) -> None:
        if not index > 0:
            raise ValueError("Index must be greater then 0")

    def guard_equal_length_of_components(self, vector_a: Vector, vector_b: Vector) -> None:
        if not len(vector_a.get_components()) == len(vector_b.get_components()):
            raise Exception("Vectors must be of the same length")

    def guard_is_a_number(self, input_of_random_type) -> None:
        try:
            self.common_validator.guard_is_a_number(input_of_random_type)
        except ValueError as value_error:
            raise value_error
