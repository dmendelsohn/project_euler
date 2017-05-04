import utils

# Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
# Warning: This takes a while (25s)
def compute(verbose=False):
    MAX = 10**7
    phis = utils.get_first_totients(MAX)
    min_ratio = MAX
    for index in range(2,len(phis)):
        phi = phis[index]
        if phi != 0 and utils.is_permutation(index, phi):
          r = 1.0*index/phi
          if r < min_ratio:
              min_ratio = r
              min_index = index
    text = "The n for which phi(n) is a permutation of n and n/phi(n) is minimized (%f)" % (min_ratio,)
    return min_index, text
