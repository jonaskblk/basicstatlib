class Vector:
    def __init__(self, components: list) -> None:
        _VectorValidator.guard_components_not_empty(components)
        _VectorValidator.guard_components_of_type_float_or_int(components)
        self.components = components

    def get_component_by_index(self, index: int) -> float:
        _VectorValidator.guard_index_greater_then_zero(index)
        return self.components[index - 1]

    def set_value_of_component(self, index: int, value: float) -> float:
        _VectorValidator.guard_index_greater_then_zero(index)
        self.components[index - 1] = value

    def add(self, vector_b: 'Vector'):
        vector_a = Vector(self.components)
        _VectorValidator.guard_equal_length_of_components(vector_a, vector_b)
        self.components = [a_i + b_i for a_i, b_i in zip(vector_a.components, vector_b.components)]

    def subtract(self, vector_b: 'Vector'):
        vector_a = Vector(self.components)
        _VectorValidator.guard_equal_length_of_components(vector_a, vector_b)
        self.components = [a_i - b_i for a_i, b_i in zip(vector_a.components, vector_b.components)]

    def multiply_with_scalar(self, scalar: float) -> None:
        pass

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
    def guard_index_greater_then_zero(index):
        if not index > 0:
            raise ValueError("Index must be greater then 0")

    @staticmethod
    def guard_equal_length_of_components(vector_a: 'Vector', vector_b: 'Vector'):
        if not len(vector_a.components) == len(vector_b.components):
            raise Exception("Vectors must be of the same length")