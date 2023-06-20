def error_bit_rate(signal_in: list[int], signal_out: list[int]) -> int:
    """ Return calculated error bit rate based on input and output signal """

    correct_bits: int = 0
    for i in range(len(signal_in)):
        if signal_in[i] == signal_out[i]:
            correct_bits += 1

    return int(((len(signal_in) - correct_bits) / len(signal_in)) * 100)
