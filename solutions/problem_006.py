# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def compute():
	a = sum([x for x in range(1,101)])**2 - sum([x**2 for x in range(1,101)])
	return a, "The difference between the sum of squares of 1,...,100 and the square of the sum"