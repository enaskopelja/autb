# Zadatak 1
> Odredite najmanji kvadratni neostatak modulo `p = 2137`.

rješenje: `5`

# Zadatak 2
> Nadite rjesenja kongruencije x^2 ≡ 1902 (mod 2137).

rješenje: `+-1804`

# Zadatak 3
> Nadite prirodne brojeve `p1`, `p2` i `q` takve da vrijedi
> 
> `max(|a - p1/q|, |b - p2/q|) < q^(-3/2)`
>
> gdje je `a = √2`, `b = √59`, `10^5 < q < 6 * 10^8`

PARI/MD:
```bash
n=2;

a=vector(n);
a[1]=sqrt(2);
a[2]=sqrt(59);

Q=10000;
C=Q^(n+1);

B=matrix(n+1, n+1);
B[1,1]=1;
for(i=2, n+1, B[i,i]=C);
for(j=2, n+1, B[j,1]=-round(C*a[j-1]));

T=qflll(B);
```

rezultat: `q = 20 521 583, p1 = 29 021 901, p2 = 157 629 270`
