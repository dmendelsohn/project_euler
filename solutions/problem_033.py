import utils
import itertools

# Find denominiator of product of digit cancelling fractions
def compute():
	results = [(a,b,c) for (a,b,c) in itertools.product(range(1,10),repeat=3) if 9*a*c + b*c == 10*a*b and a < c]
	frac = reduce(lambda (n,d),(a,b,c): (n*(10*a+b), d*(10*b+c)), results, (1,1))
	a = utils.simplify_frac(frac)[1]
	return a, "The denominator of the product of the digit cancelling fractions"
