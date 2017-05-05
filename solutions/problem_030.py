import fast
import utils

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
def compute(verbose=False):
    limit = 5*10**5 # All numbers above this are not candidates
    #a = sum(x for x in range(10, limit) if x == sum(map(lambda x: x**5, utils.get_digits(x)))) # One liner
    a = fast.p30_helper()
    return a, "Sum of all numbers that are sum of fifth powers of their digits"
