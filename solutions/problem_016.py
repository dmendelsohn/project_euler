import utils

# Compute sum of digits of 2^1000
def compute():
	return sum(utils.get_digits(2**1000)), "The sum of digits of 2^1000"
