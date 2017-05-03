import utils
import operator
from functools import reduce

# Compute d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000 (see problem definition)
def compute(verbose=False):
	arr = []
	i = 1
	while len(arr) < 10**6:
		arr += utils.get_digits(i,reverse=True)
		i += 1
	return(reduce(operator.mul, (arr[10**i-1] for i in range(7)))), 'Product of relevant digits'
