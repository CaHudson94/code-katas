"""Convert dna strings."""


def song_decoder(song):
    """."""
    print(song)
    wub_out = song.split('WUB')
    wub_less = ''
    print(wub_out)
    for word in wub_out[:]:
        if len(word) < 1:
            wub_out.remove(word)
    print(wub_out)
    for word in wub_out[0:-1]:
        if len(word) >= 1:
            wub_less = wub_less + word
            wub_less = wub_less + ' '
    wub_out_last = wub_out[-1]
    if len(wub_out_last) >= 1:
        wub_less = wub_less + wub_out_last
    return wub_less
