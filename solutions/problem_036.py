import utils

# Find sum of numbers under one million that are palindromes in both base 2 and base 10
def compute(verbose=False):
	answer = 0
	for i in range(1, 1000):
		root = utils.get_digits(i, reverse=True)  # This will be 'root' of both even and odd palindrome (in base 10)

		# Reflect root to create odd-length palindrome (last digit doesn't get repeated)
		palindrome = utils.make_number(root + root[-2::-1], reverse=True)
		if utils.is_palindrome(palindrome, base=2):
			answer += palindrome

		# Reflect root to create even-length palindrome (last digit does get repeated)
		palindrome = utils.make_number(root + root[::-1], reverse=True)
		if utils.is_palindrome(palindrome, base=2):
			answer += palindrome
	
	return answer, "Sum of double palindromes under a million"
