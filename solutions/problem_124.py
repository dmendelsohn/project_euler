import utils

# Find order-10**4 rad(n) for n in [1, 10**5]
def compute(verbose=False):
    TOTAL = 10**5
    K = 10**4
    primes = utils.get_first_primes(TOTAL+1)
    rad = [1]*(TOTAL+1)
    for p in primes:
        for n in range(p, len(rad), p):
            rad[n] *= p
    results = sorted(list(enumerate(rad))[1:], key=lambda e: e[1])
    answer = results[K-1][0]
    return answer, '{}th value when 1 <= n <= {} are sorted by rad(n)'.format(K, TOTAL)