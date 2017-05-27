import utils
import fast

def compute(verbose=False):
    MAX = 120000
    rad = [1]*MAX
    primes = utils.get_first_primes(MAX)
    for p in primes: # Compute rad(n) up to MAX using sieve
        num = p
        while num < MAX:
            rad[num] *= p
            num += p
    possible_ab = sorted(range(1, MAX), key=lambda n: rad[n])
    total = fast.p127_get_total(possible_ab, rad, MAX=MAX)
    return total, 'Sum of c for all abc hits with c < {}'.format(MAX)

