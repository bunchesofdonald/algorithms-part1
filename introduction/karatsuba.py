import math


def _number_of_digits_in(x):
    return int(math.floor(math.log10(x))) + 1


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = _number_of_digits_in(max(x, y))

    a = int(str(x)[:n/2])
    b = int(str(x)[n/2:])
    c = int(str(y)[:n/2])
    d = int(str(y)[n/2:])

    return (
        10**n * karatsuba(a, c)
        + 10**(n/2) * (karatsuba(a, d) + karatsuba(b, c))
        + karatsuba(b, d)
    )
