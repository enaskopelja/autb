from dz4.utils import convergents


def wiener_attack(n, e):
    for _, denom in convergents(e, n):
        if pow(pow(2, e, n), denom, n) % n == 2:
            return denom


if __name__ == '__main__':
    print(wiener_attack(n=17568839, e=2772667))
