from fractions import Fraction
import utils

# How many of first 1000 approximate fractional expansions of sqrt(2) have more digits in num than denom
def compute(verbose=False):
    frac = Fraction(1)
    count = 0
    for i in range(1000):
        frac = 1 + 1/(frac+1)
        if utils.num_digits(frac.numerator) > utils.num_digits(frac.denominator):
        	count += 1
    return count, 'Number of first 1000 fractional expansions of sqrt(2) with more digits in numerator than denominator'
