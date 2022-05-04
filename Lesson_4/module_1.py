from functools import reduce


def sum_integers(*args):
    numbers = map(lambda x: int(x), args)
    return reduce(lambda x, y: x + y, numbers)

