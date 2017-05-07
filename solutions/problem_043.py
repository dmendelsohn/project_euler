import numpy as np
import utils
import fast
import sys

# Find the sum of all 0 to 9 pandigital numbers with this property. (See online description)
def compute(verbose=False):
    perms = utils.permutations_1_to_n(10)
    condition = (perms[4,:]%5==0) & (perms[6,:]%2==0)  # Filter out ones that fail the 2 or 5 test
    for i in range(10):
        perms[i,:] *= (10**i)
    perms = np.sum(perms, axis=0)
    perms = np.where(condition, perms, np.zeros(perms.size)).astype(np.int64)
    perms = perms[perms != 0] # Filter out zeroes
    answer = fast.p43_sum_with_property(perms)
    return answer, 'Sum of 0-9 pandigital numbers with the property'

if __name__ == "__main__":
    verbose = False
    for arg in sys.argv:
        verbose = (verbose or "verbose" in arg)
    print(compute(verbose)[0])
