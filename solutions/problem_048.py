# Find the last 10 digits of n^n summed over n=1 to 1000
def compute():
	return sum([(i**i)%(10**10) for i in range(1,1001)])%(10**10), 'Last ten digits of sum'    
