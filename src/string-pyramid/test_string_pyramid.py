"""."""
from string_pyramid import (
    count_all_characters_of_the_pyramid,
    count_visible_characters_of_the_pyramid,
    watch_pyramid_from_above,
    watch_pyramid_from_the_side
)


def visualisation(expected_watch_from_side, expected_watch_from_above,
                  actual_watch_from_side, actual_watch_from_above):
    """."""
    print('From side correct:\n{}'.format(expected_watch_from_side))
    print('--------------------------------------')
    print('From above correct:\n{}'.format(expected_watch_from_above))
    print('--------------------------------------')
    print('From side yours:\n{}'.format(actual_watch_from_side))
    print('--------------------------------------')
    print('From above yours:\n{}'.format(actual_watch_from_above))
    assert actual_watch_from_side == expected_watch_from_side
    assert actual_watch_from_above == expected_watch_from_above


print('Basic Tests')


def test_two_char():
    """."""
    characters = '*#'
    expected_watch_from_side = ' # \n***'
    expected_watch_from_above = '***\n*#*\n***'
    actual_watch_from_side = watch_pyramid_from_the_side(characters)
    actual_watch_from_above = watch_pyramid_from_above(characters)
    visualisation(
        expected_watch_from_side, expected_watch_from_above,
        actual_watch_from_side, actual_watch_from_above
    )
    assert count_visible_characters_of_the_pyramid(characters) == 9
    assert count_all_characters_of_the_pyramid(characters) == 10


def test_three_char():
    """."""
    characters = 'abc'
    expected_watch_from_side = '  c  \n bbb \naaaaa'
    expected_watch_from_above = '''\
aaaaa
abbba
abcba
abbba
aaaaa'''
    actual_watch_from_side = watch_pyramid_from_the_side(characters)
    actual_watch_from_above = watch_pyramid_from_above(characters)
    visualisation(
        expected_watch_from_side, expected_watch_from_above,
        actual_watch_from_side, actual_watch_from_above
    )
    assert count_visible_characters_of_the_pyramid(characters) == 25
    assert count_all_characters_of_the_pyramid(characters) == 35
