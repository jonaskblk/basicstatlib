class Vector:
    def __init__(self, components: list) -> None:
        if (components.__eq__([])):
            raise ValueError("A Vector consists of at least one component")

        if (all([isinstance(component, float) for component in components])):
            self.components = components
        elif (all([isinstance(component, int) for component in components])):
            self.components = components
        else:
            raise ValueError("Components must be of type float or int")
    
    def get_component_by_index(self, index: int) -> float:
        assert index > 0, "Index must be greater then 0"
        return self.components[index - 1]

    def set_value_of_component(self, index: int, value: float) -> float:
        assert index > 0, "Index must be greater then 0"
        self.components[index - 1] = value