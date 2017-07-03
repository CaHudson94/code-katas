"""Test for proper parenthetics assesment of strings."""
from proper_parenthetics import proper_parenthetics
import pytest


STRING_PARAMS = [
    (')()()()()', -1),
    ('((())', 1),
    ('(you(are(proper)))', 0),
    ('((((()))(()))())', 0),
    ('()()(())())(', -1),
    ('))((', -1),
    ('(((()))()()()', 1),
    ('(word)(goes)here)', -1),
]


@pytest.mark.parametrize('string, result', STRING_PARAMS)
def test_for_porper_assesment_of_strings(string, result):
    """Test a string and it's return."""
    assert proper_parenthetics(string) == result


def test_bad_input_type():
    """Test for none string input."""
    with pytest.raises(TypeError):
        proper_parenthetics(1234)
