"""Convert dna strings."""


def solution(number):
    """."""
    multiples_three = list(range(3, number, 3))
    multiples_five = list(range(5, number, 5))
    for num in range(0, number):
        if num in multiples_three and num in multiples_five:
            multiples_five.remove(num)
    print(multiples_three)
    total = 0
    for num in multiples_three:
        total = total + num
        print(total)
    for num in multiples_five:
        total = total + num
        print(total)
    return total
