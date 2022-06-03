def relprime(x: int, y: int) -> bool:
    if not x > y:
        return relprime(y, x)

    while y > 0:
        q, r = divmod(x, y)
        x, y = y, r

    return x == 1


def continued_fraction(p: int, q: int):
    while q != 0:
        integer_part = p // q
        p -= integer_part * q
        p, q = q, p
        yield integer_part


def convergents(p: int, q: int):
    p_pprev, q_pprev = 0, 1
    p_prev, q_prev = 1, 0

    for a in continued_fraction(p, q):
        p = a * p_prev + p_pprev
        p_pprev,  p_prev = p_prev, p
        q = a * q_prev + q_pprev
        q_pprev, q_prev = q_prev, q
        yield p, q
