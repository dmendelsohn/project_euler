import itertools
import fast

# Compute smallest pentagonal difference between two pentagonal numbers whose sum is also pentagonal
#@profile
def compute(verbose=False):
    return fast.p44_helper()
    PENT = {n*(3*n-1)//2 for n in range(1,10**4)}
    print('oy')
    best = 10**9
    for (a,b) in itertools.product(PENT, repeat=2):
        if a+b in PENT and abs(a-b) in PENT:
        	best = min(best, abs(a-b))
        	temp = (a,b)
    return best, 'Smallest pentagonal difference between two pentagonal numbers whose sum is also pentagonal'

if __name__ == "__main__":
    print(compute())
