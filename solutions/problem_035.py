import utils

# How many circular primes are there below one million?
def compute(verbose=False):
	PRIMES = utils.get_first_primes(10**6, as_set=True)
	def is_circular_prime(x):
		digits = utils.get_digits(x)
		for i in range(len(digits)):
			if not utils.make_number(digits[i:]+digits[:i]) in PRIMES:
				return False
		return True
	return sum(map(is_circular_prime, PRIMES)), "Number of circular primes below one million"
