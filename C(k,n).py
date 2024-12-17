mod = 10**9 + 7

def factorial_mod(n, mod):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    return fact

def mod_inverse(a, mod):
    return pow(a, mod - 2, mod)

def combinations(k, n, mod):
    if k > n:
        return 0
    fact = factorial_mod(n, mod)
    denominator = (fact[k] * fact[n - k]) % mod
    return (fact[n] * mod_inverse(denominator, mod)) % mod

x, y = map(int, input().split())
result = combinations(x, y, mod)
print(result)

