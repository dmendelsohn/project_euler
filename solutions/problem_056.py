import itertools
import utils

# Maximum digital sum of a^b, where 0 < a,b < 100
def compute(verbose=False):
	ans = max(utils.sum_of_digits(a**b) for (a,b) in itertools.product(range(1,100), repeat=2))
	return ans, 'Maximum sum of digits of a^b, where 0 < a, b < 100'
