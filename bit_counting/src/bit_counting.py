"""Convert dna strings."""


def count_bits(n):
    """."""
    binary = '{0:100b}'.format(n)
    bit_count = 0
    for digit in binary:
        if digit == '1':
            bit_count += 1
    return bit_count
