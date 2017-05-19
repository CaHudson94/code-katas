"""."""
import pytest


STRING_PARAMS = {
    (3, 'stringy', 'stringystringystringy'),
    (5, 'pie', 'piepiepiepiepie'),
    (2, 'alphabet', 'alphabetalphabet'),
    (8, 'bob', 'bobbobbobbobbobbobbobbob'),
}


@pytest.mark.parametrize('reapeat, string, result', STRING_PARAMS)
def test_repeat_str(reapeat, string, result):
    from string_repeat import repeat_str
    assert repeat_str(reapeat, string) == result
