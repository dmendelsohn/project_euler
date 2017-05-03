import itertools
import utils

# Find the lowest number where swapping out 3 identical digits can yield 7 other primes
def compute(verbose=False):
	PRIMES = utils.get_first_primes(10**6, as_set=True) # Limit of 10**6 found by trial and error
	def is_root_of_8_fam(prime):
		digits = utils.get_digits(prime)
		for low in range(3): # Might be swapping 0s, 1s, or 2s
			locs = [i for i in range(len(digits)) if digits[i] == low] # Locations where low_digit appears
			if len(locs) < 3: #3
				continue
			for (i,j,k) in itertools.combinations(locs, 3):
				composites = low
				inc = 10**i + 10**j + 10**k
				for digit in range(low+1, 10):
					prime += inc
					if prime not in PRIMES:
						composites += 1
				if composites == 2: #2
					return True
		return False
	for p in sorted(PRIMES):
		if is_root_of_8_fam(p):
			return p, 'Lowest number in 8-member prime family'
	return -1, 'No answer found'
