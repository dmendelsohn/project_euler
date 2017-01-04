import utils

# Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
# Warning: This takes a while (100s)
def compute():
	def is_permutation(x,y): # Determine if x and y have digits that are permutations of one another
		return utils.get_sorted_digits(x) == utils.get_sorted_digits(y)
	MAX = 10**7
	phi = utils.get_first_totients(MAX)
	perms = [(e[0], 1.0*e[0]/e[1]) for e in enumerate(phi) if e[0] > 1 and e[1] != 0.0 and is_permutation(e[0], e[1])]  # List items are (n, n/phi(n))
	a, b = min(perms, key=lambda x: x[1])
	return a, "The n for which phi(n) is a permutation of n and n/phi(n) is minimized (%f)" % (b,)
