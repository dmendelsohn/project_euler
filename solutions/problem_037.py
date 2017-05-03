import utils

# Find sum of all forward and backward truncatable primes
def compute(verbose=False):
	MAX = 750000 # Found by trial and error
	PRIMES = utils.get_first_primes(MAX, as_set=True) # Found bound by trial and error
	def is_truncatable(n):
		for i in range(1,utils.num_digits(n)): # i is where to make the 'cut', specifically how many digits in right side
			mod = 10**i
			if n%mod not in PRIMES or n//mod not in PRIMES:
				return False
		return n >= 10 # To rule out 2, 3, 5, 7
	return sum(filter(is_truncatable, PRIMES)), 'Sum of all truncatable primes'
