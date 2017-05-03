from fractions import Fraction
import utils

# Compute sum of digits of numerator of 100th convergent in continued fraction for e
# Sequence is [2; 1 2 1  1 4 1  1 6 1 ... 1 2k 1 ...]
def compute(verbose=False):
    def seq(x):
        if x == 0:
        	return 2
        elif x%3 != 2:
        	return 1
        else:
        	return 2*(1+x//3)
    N = 100
    frac = None
    for i in range(N-1, -1, -1):
        if frac:
        	frac = 1/frac
        else: # Handle first step carefully
        	frac = Fraction(0)
        frac += seq(i)
    answer = utils.sum_of_digits(frac.numerator)
    return answer, "The sum of the digits of the %dth convergent of e" % (N,)
