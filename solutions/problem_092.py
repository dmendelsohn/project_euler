import utils

# How many starting numbers below ten million will arrive at 89 by repeatedly doing sum of squares of digits
# Notice optimization of identifying numbers by their digits, order doesn't matter
def compute():
	# Get all sorted sets of num_digits distinct digits that are >= k, as list of tuples
	def get_digit_sets(num_digits, min_value=0):
		if num_digits == 1:  # Base case
			return [(i,) for i in range(max(1,min_value),10)]  # Don't include (0,)
		results = []
		for smallest_digit in range(min_value, 10): # Consider all possible 'smallest digit'
			# Recursively find  all possible digit sets that can fill out the set
			for bigger_digits in get_digit_sets(num_digits-1, smallest_digit):
				results.append((smallest_digit,) + bigger_digits) # Add augmented set
		return results
	arrive_1 = {(0,0,0,0,0,0,1)} # This will be set of sorted digit sets that arrive at 1
	arrive_89 = {(0,0,0,0,0,8,9)} # This will be set of sorted digit sets that arrive at 89
	for digit_set in get_digit_sets(7):
		chain = set()
		while digit_set not in arrive_1 and digit_set not in arrive_89: # Continue building chain
			chain.add(digit_set)
			next_num = sum(map(lambda x: x**2, digit_set))
			digit_set = utils.get_sorted_digits(next_num)
			digit_set = (0,)*(7-len(digit_set)) + digit_set # Pad with zeroes to length 7
		if digit_set in arrive_1:
			arrive_1.update(chain)
		else:
			arrive_89.update(chain)
	num_sols = 0
	for digit_set in arrive_89:
		num_sols += utils.get_num_permutations(digit_set)
	return num_sols, 'Count of numbers that arrive at 89'
