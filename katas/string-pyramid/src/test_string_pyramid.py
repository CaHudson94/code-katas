"""Test suite for string pyramid."""
from string_pyramid import (
    count_all_characters_of_the_pyramid,
    count_visible_characters_of_the_pyramid,
    watch_pyramid_from_above,
    watch_pyramid_from_the_side
)
from random import choice, randint
from string import ascii_letters, digits, punctuation
import pytest

VALID_CHARS = '{}{}{}'.format(ascii_letters, digits, punctuation)


@pytest.fixture
def my_watch_pyramid_from_the_side(characters):
    """True pyramid from side view function."""
    width = 2 * len(characters) - 1
    output = '{{:^{}}}'.format(width).format
    return '\n'.join(output(char * dex) for char, dex in
                     zip(reversed(characters), range(1, width + 1, 2)))


@pytest.fixture
def my_watch_pyramid_from_above(characters):
    """True pyramid from above view function."""
    width = 2 * len(characters) - 1
    dex = width - 1
    result = []
    for a in range(width):
        row = []
        for b in range(width):
            minimum, maximum = sorted((a, b))
            row.append(characters[min(abs(dex - maximum), abs(0 - minimum))])
        result.append(''.join(row))
    return '\n'.join(result)


def my_count_visible_characters_of_the_pyramid(characters):
    """True visible count function."""
    return (2 * len(characters) - 1) ** 2


def my_count_all_characters_of_the_pyramid(characters):
    """True total count function."""
    return sum(a ** 2 for a in range(1, 2 * len(characters), 2))


def random_string():
    """Random string generation."""
    return ''.join(choice(VALID_CHARS) for _ in range(randint(1, 10)))


# None or Empty
def test_none_or_empty_input():
    """Test to show handling of nones and empty strings."""
    assert watch_pyramid_from_the_side(None) is None
    assert watch_pyramid_from_above(None) is None
    assert count_visible_characters_of_the_pyramid(None) == -1
    assert count_all_characters_of_the_pyramid(None) == -1
    assert watch_pyramid_from_the_side('') == ''
    assert watch_pyramid_from_above('') == ''
    assert count_visible_characters_of_the_pyramid('') == -1
    assert count_all_characters_of_the_pyramid('') == -1


# Basic Tests
def test_simple_test_cases():
    """Simple input tests."""
    characters = '1'
    assert (watch_pyramid_from_the_side(characters) ==
            my_watch_pyramid_from_the_side(characters))
    assert (watch_pyramid_from_above(characters) ==
            my_watch_pyramid_from_above(characters))
    assert count_visible_characters_of_the_pyramid(characters) == 1
    assert count_all_characters_of_the_pyramid(characters) == 1

    characters = '*#'
    assert (watch_pyramid_from_the_side(characters) ==
            my_watch_pyramid_from_the_side(characters))
    assert (watch_pyramid_from_above(characters) ==
            my_watch_pyramid_from_above(characters))
    assert count_visible_characters_of_the_pyramid(characters) == 9
    assert count_all_characters_of_the_pyramid(characters) == 10

    characters = 'abc'
    assert (watch_pyramid_from_the_side(characters) ==
            my_watch_pyramid_from_the_side(characters))
    assert (watch_pyramid_from_above(characters) ==
            my_watch_pyramid_from_above(characters))
    assert count_visible_characters_of_the_pyramid(characters) == 25
    assert count_all_characters_of_the_pyramid(characters) == 35

    characters = 'aaa'
    assert (watch_pyramid_from_the_side(characters) ==
            my_watch_pyramid_from_the_side(characters))
    assert (watch_pyramid_from_above(characters) ==
            my_watch_pyramid_from_above(characters))
    assert count_visible_characters_of_the_pyramid(characters) == 25
    assert count_all_characters_of_the_pyramid(characters) == 35

    characters = '54321'
    assert (watch_pyramid_from_the_side(characters) ==
            my_watch_pyramid_from_the_side(characters))
    assert (watch_pyramid_from_above(characters) ==
            my_watch_pyramid_from_above(characters))
    assert count_visible_characters_of_the_pyramid(characters) == 81
    assert count_all_characters_of_the_pyramid(characters) == 165


# Random
def test_random_string_input():
    """Test handling of random string inputs."""
    for _ in range(100):
        characters = random_string()
    assert (watch_pyramid_from_the_side(characters) ==
            my_watch_pyramid_from_the_side(characters))
    assert (watch_pyramid_from_above(characters) ==
            my_watch_pyramid_from_above(characters))
    assert (count_visible_characters_of_the_pyramid(characters) ==
            my_count_visible_characters_of_the_pyramid(characters))
    assert (count_all_characters_of_the_pyramid(characters) ==
            my_count_all_characters_of_the_pyramid(characters))
