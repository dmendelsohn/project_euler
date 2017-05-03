import utils

# Sum first 100 digits across all 0 < n <= 100, where n is not perfect square
def compute(verbose=False):
	def sum_of_expansion(a, n): # Sum first n digits of sqrt(a), assuming 1 <= a < 100
		a *= (10**(2*n-2))  # Need d=n-1 more digits, so multiply by 10^(2d)
		return utils.sum_of_digits(utils.isqrt(a))
	answer = sum(sum_of_expansion(i, 100) for i in range(1,101) if utils.isqrt(i)**2 != i)
	return answer, 'Sum of first 100 digits of all irrational sqrts up to sqrt(100)'
