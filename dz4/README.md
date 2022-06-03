# Zadatak 1
> U RSA kriptosustavu s javnim ključem (n, e) i tajnim eksponentom d, gdje je:
> 
> `n = 8700691, e = 7, d = 2070103`
> 
> odredite najmanji prirodan broj k takav da za broj `m = (ed − 1)/2^k` postoji neki prirodan broj `a` takav da je `nzd(a, n) = 1` i `am ≢ 1 (mod n)`. Odredite i najmanji
pripadni prirodni broj `a`.

rješenje: `a = 5, k = 2 (5^3622680 = 3955618 != 1 (mod 8700691))`  


# Zadatak 2
> Neka je `(n, e) = (17568839, 2772667)` javni RSA ključ. Poznato je da tajni eksponent
`d` zadovoljava nejednakost `d < 1/3 n^(1/4)`. Odredite `d` pomoću Wienerovog napada.

rješenje: `d = 19`

# Zadatak 3
> Odredite najmanji prirodan broj n koji je pseudoprost broj u bazi 39, a nije Eulerov
pseudoprost broj u bazi 39.

rješenje: `95`
