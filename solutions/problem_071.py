import utils
from fractions import Fraction

# Get the highest proper fraction with d <= 10^6 that's strictly less than 3/7
def compute(verbose=False):
    REF = Fraction(3,7)
    MAX_DEN = 10**6
    max_so_far = Fraction(0)
    for den in range(2, MAX_DEN+1):
        num = int(1.0 * den * REF.numerator / REF.denominator)
        if (den * REF.numerator) % REF.denominator == 0:
        	num -= 1  # need to be strictly less than REF
        max_so_far = max(max_so_far, Fraction(num,den))
    text = "Fraction immediately preceding %d/%d is %d/%d" % (REF.numerator,
        													  REF.denominator, 
        													  max_so_far.numerator,
        													  max_so_far.denominator)
    return max_so_far.numerator, text
