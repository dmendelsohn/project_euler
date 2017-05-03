import utils
import itertools


# Find denominator of product of digit cancelling fractions
def compute(verbose=False):
	# a/b, c/d are digit cancelling if 9*a*c + b*c == 10*a*b; specify a < c to avoid duplicates
	results = [(a,b,c) for (a,b,c) in itertools.product(range(1,10),repeat=3) if 9*a*c + b*c == 10*a*b and a < c]
	numer, denom = (1,1)
	for (a,b,c) in results:
		numer *= (10*a + b)
		denom *= (10*b + c)
	answer = utils.simplify_frac((numer, denom))[1]
	return answer, "The denominator of the product of the digit cancelling fractions"
