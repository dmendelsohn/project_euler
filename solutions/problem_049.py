import utils

# Get increasing 4-digit 3-element arithmetic sequence where all elements are prime and permutations of one another
def compute(verbose=False):
	PRIMES = utils.get_first_primes(10**4, as_set=True)
	DIGITS = {n:utils.get_sorted_digits(n) for n in range(10**3, 10**4)}
	for n in range(10**3, 10**4):
		if n not in PRIMES or n == 1487:
			continue # We can skip this n
		for skip in range(6, (10**4-n)//2, 6):  # Skip has to be multiple of 2 and multiple of 3
			if n in PRIMES and n+skip in PRIMES and n+2*skip in PRIMES:
				if DIGITS[n+skip] == DIGITS[n] and DIGITS[n+2*skip] == DIGITS[n]:
					return int(str(n)+str(n+skip)+str(n+2*skip)), 'Next sequence with property'
