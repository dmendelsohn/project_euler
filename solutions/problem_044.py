import itertools

# Compute smallest pentagonal difference between two pentagonal numbers whose sum is also pentagonal
def compute(verbose=False):
    PENT = {n*(3*n-1)//2 for n in range(1,10**4)}
    best = 10**9
    for (a,b) in itertools.product(PENT, repeat=2):                
        if a+b in PENT and abs(a-b) in PENT:
        	best = min(best, abs(a-b))
        	temp = (a,b)
    return best, 'Smallest pentagonal difference between two pentagonal numbers whose sum is also pentagonal'
