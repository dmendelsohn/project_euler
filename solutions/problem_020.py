import utils

# Compute sum of digits of 100!
def compute(verbose=False):
	return sum(utils.get_digits(utils.factorial(100))), "Sum of digits of 100!"
