import functools


def euclid(x, y):
    if not x > y:
        return euclid(y, x)

    while y > 0:
        q, r = divmod(x, y)
        yield q, r
        x, y = y, r


def bezout(x, y):
    return tuple(reversed(bezout(y, x))) if x < y else functools.reduce(
        lambda accum, qr: (
            accum[1],
            (
                accum[0][0] - qr[0] * accum[1][0],
                accum[0][1] - qr[0] * accum[1][1]
            )
        ),
        euclid(x, y),
        ((1, 0), (0, 1)),
    )[0]


def modular_inverse(x, m):
    return bezout(x, m)[0]
