"""."""
import pytest


DNA_PARAMS = {
    ("GTAT", "CATA"),
    ("ATTGC", "TAACG"),
    ("AAAA", "TTTT"),
    ('ATTT', 'TAAA'),
    ('CGATTA', 'GCTAAT'),
    ('GATCCTGATC', 'CTAGGACTAG'),
    ('GGGAAATTTCCCTCGAACTG', 'CCCTTTAAAGGGAGCTTGAC')
}


@pytest.mark.parametrize('dna, result', DNA_PARAMS)
def test_complimentary_dna(dna, result):
    """."""
    from complementary_dna import dna_strand
    assert dna_strand(dna) == result
