"""Make a pyramid out of a string."""


def watch_pyramid_from_the_side(characters):
    """Visual of the pyramid from the side."""
    if not characters:
        return characters
    count = 1
    char_list = []
    space_count = len(characters) - 1
    spaces = ' ' * space_count
    pyramid = ''
    for character in characters:
        char_list.append(character)
    for character in char_list[::-1]:
        pyramid += (spaces + (character * count) + spaces)
        pyramid += '\n'
        space_count -= 1
        count += 2
        spaces = ' ' * space_count
    return pyramid[:-1]


def watch_pyramid_from_above(characters):
    """Visual of the pyramid from above."""
    if not characters:
        return characters
    if len(characters) == 1:
        return characters
    pyramid = ''
    start = 0
    end = -1
    count = (len(characters) * 2) - 1
    char_list = []
    char_count = 0
    for character in characters:
        char_list.append(character)
        char_count += 1
    base = char_list[0] * count
    pyramid += base + ' ' + base
    for char in char_list[1:]:
        count -= 2
        base = base[:start + 1] + (char * count) + base[end:]
        start += 1
        end -= 1
        if char_count != 2:
            split = pyramid.split(' ')
            pyramid = split[0] + '\n' + base
            pyramid += ' ' + pyramid[::-1]
            char_count -= 1
        else:
            split = pyramid.split(' ')
            pyramid = split[0] + '\n' + base + '\n' + split[1]
    return pyramid


def count_visible_characters_of_the_pyramid(characters):
    """Count the outer characters of the pyramid."""
    if not characters:
        return -1
    count = 0
    for char in characters:
        if count == 0:
            count += 1
        else:
            count += 2
    return count ** 2


def count_all_characters_of_the_pyramid(characters):
    """Count the total characters of the pyramid."""
    if not characters:
        return -1
    count = 1
    total = 0
    for char in characters:
        total += count ** 2
        count += 2
    return total
