import utils

# Smallest number where x, 2x, 3x, 4x, 5x, 6x all have same digits
def compute():
	def fits_criteria(x):
		MAX_MULT = 6
		if utils.num_digits(x) != utils.num_digits(MAX_MULT*x):
			return False # x and 6x don't have the same number of digits
		digits = utils.get_sorted_digits(x)
		for mult in range(2, MAX_MULT+1):
			if digits != utils.get_sorted_digits(x*mult):
				return False
		return True
	x = 1
	while True:
		if fits_criteria(x):
			return x, 'Smallest number where first six multiples are all permutations'
		x += 1
