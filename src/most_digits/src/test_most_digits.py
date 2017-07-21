"""."""
import pytest


LIST_PARAMS = {
    (([1, 10, 100]), 100),
    (([9000, 8, 800]), 9000),
    (([8, 900, 500]), 900),
    (([3, 40000, 100]), 40000),
    (([1, 200, 100000]), 100000),
    (([10, 40, 300]), 300),
    (([5, 92, 17]), 92),
    (([12, 1, 4]), 12),
    (([35000, 123, 594]), 35000),
}


@pytest.mark.parametrize('num_list, result', LIST_PARAMS)
def test_find_longest(num_list, result):
    """."""
    from most_digits import find_longest
    assert find_longest(num_list) == result
