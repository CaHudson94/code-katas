"""."""
import pytest


MULT_PARAMS = {
    (10, 23),
    (33, 225),
    (61, 870),
    (79, 1428),
    (14, 45),
    (21, 98),
    (39, 329)
}


@pytest.mark.parametrize('limit, result', MULT_PARAMS)
def test_complimentary_dna(limit, result):
    """."""
    from multiples_of_3_and_5 import solution
    assert solution(limit) == result
