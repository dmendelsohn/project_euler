import math
import utils

# Print first 10 digits of massive sum
def compute(verbose=False):
    numbers = map(int, open(utils.INPUT_PATH + 'p013_numbers.txt').read().split('\n'))
    total = sum(numbers)
    total //= 10**(int(math.log10(total))-10+1)
    return total, "he first ten digits of some massive sum"
