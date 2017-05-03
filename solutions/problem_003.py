import utils

# Largest prime factor of 600851475143
def compute(verbose=False):
    INPUT = 600851475143
    return max(utils.prime_factorize(INPUT).keys()), "The largest prime factor of %d" % (INPUT,)
