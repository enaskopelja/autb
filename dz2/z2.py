"""
Riješite sustav kongruencija
x ≡ 2 (mod 7), x ≡ 2 (mod 11), x ≡ 12 (mod 13).
"""

from dz2.utils import bezout


def inductive_crt(xm, *args):
    x, m = xm
    if not args:
        return x

    (x_i, m_i), *args = args
    u, v = bezout(m, m_i)
    x = (u * x_i) * m + (v * x) * m_i
    m *= m_i
    x %= m
    return inductive_crt((x, m), *args)


if __name__ == '__main__':
    print(
        inductive_crt(
            (2, 7),
            (2, 11),
            (12, 13),
        )
    )