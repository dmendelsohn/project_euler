import itertools
import utils

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
def compute(verbose=False):
	MAX = 10**4 # Trial and error
	PRIMES = utils.get_first_primes(MAX)
	SQUARES = [i**2 for i in range(utils.isqrt(MAX))] # First squares
	sums = {p+2*s for (p,s) in itertools.product(PRIMES, SQUARES)}
	i = 3
	while (i in sums):
		i += 2
	return i, 'Smallest odd composite that cannot be written as sum of prime and twice a square'
