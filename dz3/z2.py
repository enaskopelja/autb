# Nadite rjesenja kongruencije x^2 ≡ 1902 (mod 2137).
import functools
from itertools import count

from z1 import main as find_first_quad_nonresidue


def _factor_two(x):
    for s in count():
        if x % 2:
            break
        x //= 2

    return s, x


def tonelli(a, p):
    s, t = _factor_two(p - 1)
    A, D = pow(a, t, p), pow(find_first_quad_nonresidue(p), t, p)

    powers = [2**i for i in range(s)]

    m = functools.reduce(
        lambda prev, curr: prev + (
            curr[0]
            if pow(A * pow(D, prev, p), curr[1], p) == p - 1
            else 0
        ),
        zip(powers, reversed(powers)),
        0
    )
    return (pow(a, (t + 1) // 2, p) * pow(D, m // 2, p)) % p


def solve_modular_quad_root(a, p):
    a %= p

    if p % 8 in {3, 7}:
        return pow(a, (p + 1) // 4, p)

    if p % 8 == 5:
        x = pow(a, (p + 3) // 8, p)
        c = x ** 2 % p
        return x if c % p == a else x * pow(2, (p - 1) // 4, p)

    return tonelli(a, p)


def main():
    a, p = 1902, 2137
    result = solve_modular_quad_root(a, p)
    assert pow(result, 2, p) == a
    print(result)


if __name__ == '__main__':
    main()
