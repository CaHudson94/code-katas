"""."""
import pytest


SENT_PARAMS = {
    ('Welcome', 'emocleW'),
    ('Never going to give you up', 'reveN gniog to give you up'),
    ('Never going to let you down', 'reveN gniog to let you down'),
    ('Whimsical words', 'lacismihW sdrow'),
    ('Hi', 'Hi')
}


@pytest.mark.parametrize('sentence, result', SENT_PARAMS)
def test_complimentary_dna(sentence, result):
    """."""
    from stop_gninnips_my_sdrow import spin_words
    assert spin_words(sentence) == result
