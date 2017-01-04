import utils

def compute():
	def get_pandigital_mult(n):
		mult = 0
		digits = []
		while (len(digits) < 9):
			mult += 1
			digits += utils.get_digits(n*mult, reverse=True)
		if sorted(digits) == range(1,10) and mult > 1:
			return utils.make_number(digits, reverse=True)
		else:
			return 0
	return max(get_pandigital_mult(i) for i in range(1,10**4)), ''
