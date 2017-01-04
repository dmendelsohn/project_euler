import utils

# Compute how many n-digits numbers are an n-th power of an integer
def compute():
	results = [1]  # Account for base = 1
	for b in range(2, 10):  # Only other possible bases are 2...9, 10^n always has n+1 digits
		n = 1
		while utils.num_digits(b**n) == n:  # As long as the exponent still has right number of digits
			results.append(b**n)
			n += 1
	return len(set(results)), 'Number of n-digit numbers that are nth power of an integer'
