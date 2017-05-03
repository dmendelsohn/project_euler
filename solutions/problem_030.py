import utils

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
def compute(verbose=False):      
	a = sum(x for x in range(10, 10**6) if x == sum(map(lambda x: x**5, utils.get_digits(x))))
	return a, "Sum of all numbers that are sum of fifth powers of their digits"
