import pytest
from qlib.math.common import CommonValidator


class TestCommonValidator:

    @pytest.mark.parametrize("possible_number", [
        (
            -1
        ),
        (
            0
        ),
        (
            1
        ),
        (
            33
        ),
    ])
    def test_guard_is_a_number(self, possible_number) -> None:
        common_validator = CommonValidator()
        common_validator.guard_is_a_number(possible_number)
