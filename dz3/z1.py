# Odredite najmanji kvadratni neostatak modulo p = 2137.
from itertools import count


def _make_odd(a: int) -> tuple[int, int]:
    for alpha in count():
        if a % 2:
            break
        a //= 2

    return a, alpha


def _check_cond(a: int, m: int, alpha: int) -> bool:
    return (
        (alpha % 2 and (m % 8 in {3, 5})) ^
        (a % 4 == 3 and m % 4 == 3)
    )


def jacobi(a: int, m: int) -> int:
    assert m > 0 and m % 2 == 1
    a %= m
    if a == 0:
        return int(m == 1)

    a, alpha = _make_odd(a)
    return (
               -1 if _check_cond(a, m, alpha) else 1
           ) * jacobi(m, a)


def main(p: int) -> int:
    for a in range(p):
        if jacobi(a, p) == -1:
            return a

    raise RuntimeError("Not found")


if __name__ == '__main__':
    print(main(2137))
