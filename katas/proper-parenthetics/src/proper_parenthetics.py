"""Test strings of parens to see if the are open, balanced, or closed."""
from stack import Stack


def proper_parenthetics(parens):
    """Function to check open and close parens."""
    if type(parens) != str:
        raise TypeError('This must be a string.')
    paren_list = Stack(parens[::-1])
    open_paren = 0
    close_paren = 0
    pops = 0
    while pops != len(parens):
        popped = paren_list.pop()
        if popped == '(':
            open_paren += 1
        elif popped == ')':
            close_paren += 1
        if close_paren > open_paren:
            return -1
        pops += 1
    if open_paren > close_paren:
        return 1
    return 0
