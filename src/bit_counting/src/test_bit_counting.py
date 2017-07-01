"""."""
import pytest


BIT_PARAMS = {
    (0, 0),
    (4, 1),
    (7, 3),
    (9, 2),
    (10, 2),
    (25, 3),
    (4525, 7),
    (897521, 12),
    (3, 2)
}


@pytest.mark.parametrize('number, result', BIT_PARAMS)
def test_bit_counting(number, result):
    """."""
    from bit_counting import count_bits
    assert count_bits(number) == result
