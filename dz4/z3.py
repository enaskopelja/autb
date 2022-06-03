# Odredite najmanji prirodan broj n koji je pseudoprost broj u bazi 39, a nije Eulerov
# pseudoprost broj u bazi 39.
import math
from itertools import count

from dz3.z1 import jacobi


def odd(n: int) -> bool:
    return n % 2 == 1


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def _odd_composite_gcd_1(n, b):
    return n % 2 == 1 and (not prime(n)) and math.gcd(b, n) == 1


def euler_pseudoprime(n, b):
    if not _odd_composite_gcd_1(n, b):
        return False
    return pow(b, (n - 1) // 2, n) % n == jacobi(b, n) % n


def pseudoprime(n, b):
    if not _odd_composite_gcd_1(n, b):
        return False
    return pow(b, n - 1, n) % n == 1


def main(base: int) -> int:
    for n in count(start=4):
        if (
            pseudoprime(n, base) and
            not euler_pseudoprime(n, base)
        ):
            return n


if __name__ == '__main__':
    print(main(39))

