import operator
import utils

# Find highest product of 13 consecutive digits in big number from the problem
def compute():
	s = open(utils.INPUT_PATH + "p008_digits.txt").read().replace('\n','')
	return max(reduce(operator.mul, map(int, s[i:i+13])) for i in range(len(s)-13+1)), "Highest product"
