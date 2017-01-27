import itertools
import utils

# What is largest n-digit pandigital prime?
def compute():
	best = 0
	for num_digits in range(1,10):
		for perm in itertools.permutations(range(1, num_digits + 1)):
			num = utils.make_number(perm, reverse=True)
			if utils.is_prime(num):
				best = num
	return best, 'Largest n-digit pandigital prime'
