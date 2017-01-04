import utils

# Find sum of numbers under one million that are palindromes in both base 2 and base 10
def compute():
	answer = 0
	for i in range(1, 1000):
		d = utils.get_digits(i, reverse=True)  # This will be base of both even and odd palindrome (in base 10)
		for num in map(lambda x: utils.make_number(x, reverse=True), [d+d[-2::-1], d+d[::-1]]):
			if utils.is_palindrome(num, base=2):  # Check if it's also a base 2 palindrome
				answer += num
	return answer, "Sum of double palindromes under a million"
