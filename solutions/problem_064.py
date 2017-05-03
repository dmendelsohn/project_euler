import math
import utils
from functools import reduce

# Compute how many N < 10^4 have odd-length cycles in partial fraction approx. sequence
def compute(verbose=False):
	def rationalize(num, tup):  # Takes in fraction of form num / (a*sqrt(b)+c); tup = (a,b,c)
		(a, b, c) = tup
		num = (num*a, b, -num*c)
		den = a*a*b - c*c
		return (num, den)

	def divide(num, div):  # num could be int for 3-tuple
		if isinstance(num, int):
			return num//div
		else: # it's a 3-tuple
			return (num[0]//div, num[1], num[2]//div)

	def simplify(num, den):
		numbers = []
		for x in [num, den]:
			if isinstance(x, int):
				numbers.append(x)
			else: # It's a 3-tuple
				numbers.append(x[0])
				numbers.append(x[2])
		gcd = reduce(utils.gcd, numbers)
		return divide(num, gcd), divide(den, gcd)

	def floor(tup, den):
		(a, b, c) = tup
		return int((a*math.sqrt(b)+c)//den)

	def next_step(num, tup): # (num/(a*sqrt(b)+c) is current state; tup = (a,b,c)
		(a, b, c), den = rationalize(num, tup)
		s = floor((a,b,c), den)
		c -= s*den
		num, den = simplify((a,b,c), den)  # num is 3-tuple
		return (s, den, num)

	def init_step(x):
		sqrt = utils.isqrt(x)
		return (sqrt, 1, (1, x, -sqrt))

	def get_cycle_len(x): # Assume x is not a perfect square
		step_list = []
		seen = {}
		step = init_step(x)
		count = 0
		while step not in seen:
			step_list.append(step)
			seen[step] = count
			count += 1
			step = next_step(step[1],step[2]) # next_step(num, (a,b,c))
		return len(step_list) - seen[step]  # Return cycle length

	squares = set([x**2 for x in range(1, 101)])
	MAX = 10**4
	ans = sum(1 for x in range(2, MAX+1) if x not in squares and get_cycle_len(x)%2==1)
	return ans, "Count of irrational roots, up to sqrt(%d), with odd-length rational approximation cycle" % (MAX,)
