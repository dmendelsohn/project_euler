import operator
import utils
from functools import reduce

# Find highest product of 13 consecutive digits in big number from the problem
def compute(verbose=False):
    num_str = open(utils.INPUT_PATH + "p008_digits.txt").read().replace('\n','')
    high = 0
    for i in range(len(num_str)-13+1):
        product = reduce(operator.mul, map(int, num_str[i:i+13]))
        high = max(high, product)
    return high, 'Highest product'
