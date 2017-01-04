import utils

# Find the largest palindrome made from the product of two 3-digit numbers.
def compute():
	def check_palindrome(arr):
		if len(arr) < 2:
			return True
		elif arr[0]!=arr[-1]:
			return False
		else:
			return check_palindrome(arr[1:len(arr)-1])
	a = max(reduce(max, [i*j for j in range(i, 1000) if check_palindrome(utils.get_digits(i*j))], 0) for i in range(100, 1000))
	return a, "The largest palindrome made from the product of two 3-digit numbers"
