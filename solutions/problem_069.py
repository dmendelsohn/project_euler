import utils

# Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
def compute(verbose=False):
    MAX = 10**6
    phi = utils.get_first_totients(MAX)
    results = [1] + [1.0*phi[i]/i for i in range(1, len(phi))]
    a = results.index(min(results))
    return a, "The n less than one million that yeilds the highest n/phi(n) (which is %f)" % (1.0/results[a],)
