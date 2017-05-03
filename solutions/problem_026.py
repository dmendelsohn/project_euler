# Find d < 1000 for which 1/d has longest repeating cycle
def compute(verbose=False):
    NINES = [10**i-1 for i in range(1,1500)]
    def length_of_repeat(x):
        if (x%2 == 0 or x%5==0):
        	return 0 # These terminate
        for i in range(len(NINES)):
        	if NINES[i]%x==0:
        		return i+1
    arr = [length_of_repeat(i) for i in range(1000)]
    a = arr.index(max(arr))
    return a, "The d < 1000 for which 1/d has the longest repeating cycle"
