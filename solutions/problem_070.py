import utils

# Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
# Warning: This takes a while (100s)
def compute(verbose=False):
    def is_permutation(x,y): # Determine if x and y have digits that are permutations of one another
        return utils.get_sorted_digits(x) == utils.get_sorted_digits(y)
    MAX = 10**7
    phis = utils.get_first_totients(MAX)
    perms = []
    for (index, phi) in enumerate(phis):
        if index > 1 and phi != 0.0 and is_permutation(index, phi):
        	perms.append((index, 1.0*index/phi))
    n, ratio = min(perms, key=lambda x: x[1])
    text = "The n for which phi(n) is a permutation of n and n/phi(n) is minimized (%f)" % (ratio,)
    return n, text
