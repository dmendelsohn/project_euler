import utils

# R(d) is essentially phi(d)/(d-1)
# Find least d such that R(d) < 15499/94744
def compute(verbose=False):
    # Observation, number is going to basically be produt of unique primes.  Non-unique prime factors
    # help very, very, very slightly, and the threshold is contrived so that matters.
    THRESH = 15499/94744
    primes = utils.get_first_primes(50) # 15 primes is more than enough
    d = 1
    phi = 1
    for p in primes:
        d *= p
        phi *= (p-1)
        for mult in range(1, p): # Before moving onto next prime, try all non-unique factors
            if mult*phi/(mult*d-1) < THRESH:
                return mult*d, 'Least d for which R(d) < 15499/94744'
    return -1, 'Could not find solution'
