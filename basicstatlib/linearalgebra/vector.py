class Vector:
    def __init__(self, components: list) -> None:
        self.__guard_components_not_empty(components)
        self.__guard_components_of_type_float_or_int(components)

        self.components = components
    
    def __guard_components_not_empty(self, components: list) -> None:
        if (components.__eq__([])):
            raise ValueError("A Vector consists of at least one component")

    def __guard_components_of_type_float_or_int(self, components: list) -> None:
        if (all([isinstance(component, float) for component in components])):
            pass
        elif (all([isinstance(component, int) for component in components])):
            pass
        else:
            raise ValueError("Components must be of type float or int")

    def get_component_by_index(self, index: int) -> float:
        assert index > 0, "Index must be greater then 0"
        return self.components[index - 1]

    def set_value_of_component(self, index: int, value: float) -> float:
        assert index > 0, "Index must be greater then 0"
        self.components[index - 1] = value

    def add(self, vector_b: 'Vector'):
        vector_a = Vector(self.components)
        assert len(vector_a.components) == len(vector_b.components), "Vectors must be of the same length"
        self.components = [a_i + b_i for a_i, b_i in zip(vector_a.components, vector_b.components)]

    def subtract(self, vector_b: 'Vector'):
        vector_a = Vector(self.components)
        assert len(vector_a.components) == len(vector_b.components), "Vectors must be of the same length"
        self.components = [a_i - b_i for a_i, b_i in zip(vector_a.components, vector_b.components)]