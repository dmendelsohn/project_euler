import utils

def compute(verbose=False):
    PRIMES = utils.get_first_primes(10**6)  # This ought to be plenty
    THRESH = 10**10
    for n in range(1,len(PRIMES),2):
        p = PRIMES[n-1]
        if (2*n*p)%(p**2) > THRESH:
            return n, 'Least n for which (p_n + 1)^n + (p_n - 1)^n mod (p_n)^2 is > 10^10'
    return -1, 'Could not find answer'