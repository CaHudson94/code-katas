"""."""
import pytest


WUB_PARAMS = {
    ("AWUBBWUBC", "A B C"),
    ("AWUBWUBWUBBWUBWUBWUBC", "A B C"),
    ("WUBAWUBBWUBCWUB", "A B C"),
    ('WUBWUBWUBWUBRWUBUWUBCWUBOWUBOWUBL', 'R U C O O L'),
    ('WUBMEWUB', 'ME'),
    ('WWUBWWUBWUBE', 'W W E'),
    ('YWUBOWUBUWUB', 'Y O U')
}


@pytest.mark.parametrize('wub, result', WUB_PARAMS)
def test_bit_counting(wub, result):
    """."""
    from dubstep import song_decoder
    assert song_decoder(wub) == result
