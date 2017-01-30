import math
import operator
from itertools import chain
from functools import reduce

# Find sum of minimal product-sum numbers for 2<=k<=12000
# Slow-ish (10s)
def compute():
	# Returns list of sorted tuples that fit constraints, numbers must  be ints > 0
	def get_multisets(max_sum, max_prod, max_elt, num_elts):
		if num_elts == 0: # We're done!
			return [()]  # Base case with single solution: the empty multiset
		elif max_prod < 1 or max_sum < 1:
			return []  # Base case: no solutions since we can't fit enough numbers in
		results = []
		highest_possible = min(max_elt, int(max_prod), max_sum)
		for i in range(1, 1+highest_possible):  # Let's use i as largest element of tuple, and solve recursively
			results.extend(map(lambda t: t+(i,), get_multisets(max_sum-i, 1.0*max_prod/i, i, num_elts-1)))
		return results
	K = 12000
	sols = {k:2*k for k in range(2,K+1)}  # Baseline solutions (1,1,1,1....,1,2,k), where there are k-2 1's
	max_size = int(math.log(2*K, 2)) # All the rest of them must be 1
	multisets = get_multisets(K+max_size, 2*K, K, max_size)
	for m in multisets:
		prod = reduce(operator.mul, m, 1)
		k = len(m) + prod - sum(m)  # Pad with prod - sum(m) ones to make product = sum
		if k in sols:
			sols[k] = min(sols[k], prod)  # maybe improve minimal product-sum with k elements
	ans = sum(set(sols.values()))  # Sum the unique values
	return ans, 'Sum of minimal product-sum number for 2<=k<=12000'
