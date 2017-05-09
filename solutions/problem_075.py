import utils
import fast

# How many L < 1.5 million are sum of EXACTLY ONE Pythagorean triple
def compute(verbose=False):
    answer = fast.p75_helper()
    return answer, "Number of L < 1.5 million that are the sum of exactly one Pythagorean triple"
