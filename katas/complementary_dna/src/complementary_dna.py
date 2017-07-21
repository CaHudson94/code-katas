"""Convert dna strings."""


def dna_strand(dna):
    """Change the letters."""
    return_dna = ''
    for letter in dna:
        if letter == 'A':
            return_dna = return_dna + 'T'
        elif letter == 'T':
            return_dna = return_dna + 'A'
        elif letter == 'C':
            return_dna = return_dna + 'G'
        elif letter == 'G':
            return_dna = return_dna + 'C'
    return return_dna
