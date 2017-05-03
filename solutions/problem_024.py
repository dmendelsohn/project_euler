import utils

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
def compute(verbose=False):
	perm = utils.get_permutation(range(10), 10**6-1)
	ans = utils.make_number(perm, reverse=True)
	return ans, 'Millionth lexicographic permutation of 0...9'
