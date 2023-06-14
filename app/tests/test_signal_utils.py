from utils.signal_utils import error_bit_rate

class TestSignalUtils:
    def test_error_bit_rate(self) -> None:
        # GIVEN
        test_inputs: list[tuple[list[int], list[int], int]] = [
            ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 100),
            ([1, 1, 1, 1, 1], [1, 1, 0, 0, 1], 60)
        ]

        # WHEN

        # THEN
        for signal_in, signal_out, percent in test_inputs:
            assert error_bit_rate(signal_in, signal_out) == percent
