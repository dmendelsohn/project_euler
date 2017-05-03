import utils

# How many (not necessarily distinct) values of nCr > 10**6, n in [1,100], r in [0,n]
def compute(verbose=False):
    FACTS = utils.get_first_factorials(101)
    def get_min_r(n, cutoff): # Return minimum r for which nCr > cutoff
        for r in range(0, n+1):
        	if FACTS[n] // (FACTS[r]*FACTS[n-r]) > cutoff:
        		return r
        return -1
    def get_num_r(n, cutoff): # Return number of r for which nCr > cutoff
        min_r = get_min_r(n, cutoff)
        if min_r < 0:
        	return 0
        elif n%2==1:
        	return 2*(n//2 - min_r + 1)
        else:
        	return 2*(n//2 - min_r + 1) - 1
    answer = sum([get_num_r(n, 10**6) for n in range(1, 101)])
    return answer, 'Number of values of nCr > one million, for n,r < 100'
