import utils
from functools import reduce

# Find the largest palindrome made from the product of two 3-digit numbers.
def compute(verbose=False):
	def check_palindrome(arr):
		if len(arr) < 2:
			return True
		elif arr[0]!=arr[-1]:
			return False
		else:
			return check_palindrome(arr[1:len(arr)-1])
	high = 0
	for i in range(100, 1000):
		for j in range(i, 1000):
			if i*j > high and check_palindrome(utils.get_digits(i*j)):
					high = i*j
	return high, "The largest palindrome made from the product of two 3-digit numbers"
