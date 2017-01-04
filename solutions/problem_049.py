import utils

# Get increasing 4-digit 3-element arithmetic sequence where all elements are prime and permutations of one another
def compute():
	PRIMES = utils.get_first_primes(10**4, as_set=True)
	DIGITS = {n:utils.get_sorted_digits(n) for n in range(10**3, 10**4)}
	for n in range(10**3, 10**4):
		if n not in PRIMES or n == 1487:
			continue # We can skip this n
		for a in range(6, (10**4-n)/2, 6):  # Skip has to be multiple of 2 and multiple of 3
			if n in PRIMES and n+a in PRIMES and n+2*a in PRIMES:
				if DIGITS[n+a] == DIGITS[n] and DIGITS[n+2*a] == DIGITS[n]:
					return int(str(n)+str(n+a)+str(n+2*a)), 'Next sequence with this property'
