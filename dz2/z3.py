"""
Nadite najmanji prirodan broj d sa svojstvom da je duljina perioda u razvoju u
jednostavni verizni razlomak broja √d jednaka 16.
"""

import itertools
import math
from itertools import count

from tqdm import tqdm


def _is_palindrome(seq):
    seq_len = len(seq)
    for i in range(seq_len // 2):
        if seq[i] != seq[seq_len - i - 1]:
            return False
    return True


def continued_fraction(d):
    sqrtd = math.sqrt(d)

    if sqrtd == math.floor(sqrtd):
        return 1, [int(sqrtd)]

    def calc_params(s, t):
        a = math.floor((s + sqrtd) / t)

        s_new = a * t - s
        t_new = (d - s_new ** 2) / t
        return (a,), s_new, t_new

    def state_generator(state, s, t):
        a, s, t = calc_params(s, t)
        future = state + a

        yield state, future
        yield from state_generator(future, s, t)

    return tuple(
        itertools.takewhile(
            lambda states: (
                states[0][-1] != states[0][0] * 2 or not
                _is_palindrome(states[0][1:-1])
            ),
            state_generator(*calc_params(0, 1)),
        )
    )[-1][-1]


def main():
    for d in tqdm(count(2)):
        continued_frac = continued_fraction(d)
        if len(continued_frac) == 18:
            return d, continued_frac


if __name__ == '__main__':
    print(*main())
