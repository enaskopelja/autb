"""
Neka je R = 1000 te m = 209.
Nadite najmanji prirodan broj T > 2000 takav da je
u Montgomeryjevoj redukciji broj (T + Um)/R − (T*R^(−1) mod m) jednak m.
"""

from itertools import count
from tqdm import tqdm

from dz2.utils import modular_inverse


def _calc_U(T, m_, R):
    return (T * m_) % R


def montgomery_diff(T, m, m_, R, R_):
    return (T + _calc_U(T, m_, R) * m) / R - ((T * R_) % m)


def main(R, m):
    for T in tqdm(count(start=2000)):
        if montgomery_diff(
            T=T,
            R=R,
            m=m,
            R_=modular_inverse(R, m),
            m_=-modular_inverse(m, R),
        ) != 0:
            return T


if __name__ == '__main__':
    print(main(R=1000, m=209))
