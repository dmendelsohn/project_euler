import utils
import fast

# Find the sum of all numbers which are equal to the sum of the factorial of their digits
def compute(verbose=False):
#    FACT = utils.get_first_factorials(10)
#    a = sum(i for i in range(10, 7*FACT[9]) if i == sum(FACT[d] for d in utils.get_digits(i)))
    a = fast.p34_helper()
    return a, "Sum of all numbers that are equal to sum of the factorial of their digits"
