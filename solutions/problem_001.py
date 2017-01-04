# Find the sum of all the multiples of 3 or 5 below 1000.
def compute():
	return sum(n for n in range(1000) if n%3==0 or n%5==0), "The sum of all multiples of 3 or 5 below 1000"