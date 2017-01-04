import utils

# What is largest n-digit pandigital prime?
def compute():
	best = 0
	for n in range(1,10):
		for i in range(utils.factorial(n)):
			perm = utils.get_permutation(range(1,n+1), i)
			num = utils.make_number(perm, reverse=True)
			if utils.is_prime(num):
				best = num
	return best, 'Largest n-digit pandigital prime'
