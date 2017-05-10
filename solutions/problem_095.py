import fast

# Consider all looping chains by iteratively taking sum of proper divisors of a number.  What's the
# minimum element in the longest chain that has no value exceeding one million?
def compute(verbose=False):
    ans = fast.p95_helper()
    return ans, 'Minimum element in longest "sum of proper divisors" chain'