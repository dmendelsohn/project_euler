import utils

# How many Lychrel #s below 10^4?
def compute():
	def apply_step(x):
		return x + utils.make_number(utils.get_digits(x, reverse=True))  # Add its reverse
	def is_lychrel(x):
		for i in range(50):
			x = apply_step(x)
			if utils.is_palindrome(x):
				return False
		return True
	return len(filter(is_lychrel, range(1,10**4))), 'Number of Lychrel numbers below 10^4'
