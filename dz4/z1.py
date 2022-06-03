from itertools import count
from typing import Optional

from dz4.utils import relprime


def generate_relprimes(n):
    for a in range(n):
        if relprime(a, n):
            yield a


def generate_k_relprimes(n, k):
    yield from [
        y for x, y in zip(
            range(k),
            generate_relprimes(n),
        )
    ]


def check(m: int, n: int) -> Optional[int]:
    for a in generate_k_relprimes(n=n, k=10):
        if (p := pow(a, m, n) % n) != 1:
            print(
                f"found a = {a} s.t. "
                f"{a}^{m} = {p} != 1 (mod {n}) "
            )
            return a


def min_k(*, n, e, d):
    m = e * d - 1

    for k in count(start=1):
        m //= 2
        if (a := check(m, n)) is not None:
            return a, k


if __name__ == '__main__':
    print(min_k(n=8700691, e=7, d=2070103))
