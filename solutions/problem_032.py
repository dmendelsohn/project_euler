import utils
import itertools

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
def compute(verbose=False):
    def is_pandigital(a,b):
        combined_digits = utils.get_digits(a) + utils.get_digits(b) + utils.get_digits(a*b)
        return sorted(combined_digits) == list(range(1,10))
    memo = set()
    for (a,b,c,d,e) in itertools.permutations(range(1,10), 5):
        if is_pandigital(10*a+b, 100*c+10*d+e):
        	memo.add((10*a+b)*(100*c+10*d+e))
        elif is_pandigital(a, 1000*b + 100*c + 10*d + e):
        	memo.add(a*(1000*b+100*c+10*d+e))
    return sum(memo), "Sum of all pandigital products"
