import utils

# Find the sum of all the primes below two million.
def compute(verbose=False):
    return sum(utils.get_first_primes(2*10**6)), "The sum of all primes below two million"
