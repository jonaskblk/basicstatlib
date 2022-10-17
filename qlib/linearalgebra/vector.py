class Vector:
    def __init__(self, components: list) -> None:
        _VectorValidator.guard_components_not_empty(components)
        _VectorValidator.guard_components_of_type_float_or_int(components)
        self.__components = components

    def __eq__(self, other: 'object') -> bool:
        _VectorValidator.guard_is_of_type_vector(other)
        if (self.__components.__eq__(other.get_components())):
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.__components.__str__()

    def __repr__(self) -> str:
        return f"Vector({self.__str__()})"

    def get_components(self) -> list:
        return self.__components

    def get_component_by_index(self, index: int) -> float:
        _VectorValidator.guard_index_greater_then_zero(index)
        return self.__components[index - 1]

    def set_value_of_component(self, index: int, value: float) -> float:
        _VectorValidator.guard_index_greater_then_zero(index)
        self.__components[index - 1] = value

    def add(self, vector_b: 'Vector'):
        vector_a = Vector(self.__components)
        _VectorValidator.guard_equal_length_of_components(vector_a, vector_b)
        self.__components = [a_i + b_i for a_i, b_i in zip(vector_a.get_components(), vector_b.get_components())]

    def subtract(self, vector_b: 'Vector'):
        vector_a = Vector(self.__components)
        _VectorValidator.guard_equal_length_of_components(vector_a, vector_b)
        self.__components = [a_i - b_i for a_i, b_i in zip(vector_a.get_components(), vector_b.get_components())]

    def multiply_with_scalar(self, scalar: float) -> None:
        _VectorValidator.guard_is_a_number(scalar)
        vector = Vector(self.__components)
        self.__components = [index * scalar for index in vector.get_components()]

    def sum_of_squares(self) -> float:
        pass

    def magnitude(self) -> float:
        pass

    def magnitude(self, vector_b: 'Vector') -> float:
        pass

    def squared_distance(self, vector_b: 'Vector') -> float:
        pass

    @staticmethod
    def sum_up_vectors(vectors: list['Vector']) -> 'Vector':
        pass

    @staticmethod
    def mean_of_vectors(vectors: list['Vector']) -> 'Vector':
        pass

class _VectorValidator:
    @staticmethod
    def guard_components_not_empty(components: list) -> None:
        if (components.__eq__([])):
            raise Exception("A Vector consists of at least one component")

    @staticmethod
    def guard_components_of_type_float_or_int(components: list) -> None:
        if (all([isinstance(component, float) for component in components])):
            pass
        elif (all([isinstance(component, int) for component in components])):
            pass
        else:
            raise ValueError("Components must be of type float or int")

    @staticmethod
    def guard_is_of_type_vector(object_to_check: object) -> None:
        if not (isinstance(object_to_check, Vector)):
            raise ValueError("Object must be of type vector")

    @staticmethod
    def guard_index_greater_then_zero(index) -> None:
        if not index > 0:
            raise ValueError("Index must be greater then 0")

    @staticmethod
    def guard_equal_length_of_components(vector_a: Vector, vector_b: Vector) -> None:
        if not len(vector_a.get_components()) == len(vector_b.get_components()):
            raise Exception("Vectors must be of the same length")
    
    @staticmethod
    def guard_is_a_number(input) -> None:
        if (isinstance(input, float)):
            pass
        elif (isinstance(input, int)):
            pass
        else:
            raise ValueError("Input must be of type float or int")