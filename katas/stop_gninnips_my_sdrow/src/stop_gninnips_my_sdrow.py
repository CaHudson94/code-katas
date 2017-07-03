"""Convert dna strings."""


def spin_words(sentence):
    """."""
    words = sentence.split(' ')
    new_sentence = ''
    if len(words) < 2:
        for word in words:
            if len(word) > 4:
                word = word[::-1]
                new_sentence = new_sentence + word
            else:
                new_sentence = new_sentence + word
    elif len(words) >= 2:
        for word in words[0:-1]:
            if len(word) > 4:
                word = word[::-1]
                new_sentence = new_sentence + word + ' '
            else:
                new_sentence = new_sentence + word + ' '
        word = words[-1]
        if len(word) > 4:
            word = word[::-1]
            new_sentence = new_sentence + word
        else:
            new_sentence = new_sentence + word
    return new_sentence
