import math
import utils

# Print first 10 digits of massive sum
def compute():
	s = sum(map(int, open(utils.INPUT_PATH + 'p013_numbers.txt').read().split('\n')))
	s /= 10**(int(math.log10(s))-10+1)
	return s, "he first ten digits of some massive sum"
