"""Return the longest int in list."""


def find_longest(arr):
    """Convert int to string find the longest."""
    new_list = []
    for num in arr:
        num = str(num)
        new_list.append(num)
        longest = max(new_list, key=len)
    return int(longest)
