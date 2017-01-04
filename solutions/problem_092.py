import utils

# How many starting numbers below ten million will arrive at 89 by repeatedly doing sum of squares of digits
# Notice optimization of identifying numbers by their digits, order doesn't matter
def compute():
	def get_digit_sets(n, k=0):  # Get all sorted sets of n digits that are at least k, as list of tuples
		if n == 1:  # Base case
			return [(i,) for i in range(max(1,k),10)]  # Don't return singleton zero
		results = []
		for digit in range(k,10):
			results.extend(map(lambda t: (digit,)+t, get_digit_sets(n-1,digit)))
		return results
	A = {(0,0,0,0,0,0,1)} # A will be set of numbers that arrive at 1
	B = {(0,0,0,0,0,8,9)} # B will be set of numbers that arrive at 89
	for digits in get_digit_sets(7):
		chain = set()
		while digits not in A and digits not in B: # Build the chain based on i
			chain.add(digits)
			next_num = sum(map(lambda x: x**2, digits))
			digits = utils.get_sorted_digits(next_num)
			digits = (0,)*(7-len(digits)) + digits # Pad with zeroes
		if digits in A:
			A.update(chain)
		else:
			B.update(chain)
	return sum(utils.get_num_permutations(digits) for digits in B), 'Count of numbers that arrive at 89'
