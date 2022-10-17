"""Contains common types and procedures e.g. utils and validators for the surronding package.
"""


class CommonValidator:
    """Defines objects of type CommonValidator.
    """

    def __init__(self) -> None:
        pass

    def guard_is_a_number(self, input_of_random_type) -> None:
        """Ensures that input is only of type float or int.

        Raises:
            ValueError: Input must be of type float or int.
        """
        if (isinstance(input_of_random_type, float)):
            pass
        elif (isinstance(input_of_random_type, int)):
            pass
        else:
            raise ValueError("Input must be of type float or int")
