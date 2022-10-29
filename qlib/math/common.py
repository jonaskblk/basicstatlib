class CommonValidator:

    def __init__(self) -> None:
        pass

    def guard_is_a_number(self, input_of_random_type) -> None:
        if (isinstance(input_of_random_type, float)):
            pass
        elif (isinstance(input_of_random_type, int)):
            pass
        else:
            raise ValueError("Input must be of type float or int")
