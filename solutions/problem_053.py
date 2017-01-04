import utils

# How many (not necessarily distinct) values of nCr > 10**6, n in [1,100], r in [0,n]
def compute():
	FACTS = utils.get_first_factorials(101)
	def get_min_r_large_fact(n, cutoff):
		for r in range(0, n+1):
			if FACTS[n] / (FACTS[r]*FACTS[n-r]) > 10**6:
				return r
		return -1
	def get_num_r_large_fact(n, cutoff): # Return number of r for which nCr > cutoff
		min_r = get_min_r_large_fact(n, cutoff)
		if min_r < 0:
			return 0
		elif n%2==1:
			return 2*(n/2 - min_r + 1)
		else:
			return 2*(n/2 - min_r + 1) - 1
	return sum([get_num_r_large_fact(n, 10**6) for n in range(1,101)]), 'Number of values of nCr > one million, for n,r < 100'
