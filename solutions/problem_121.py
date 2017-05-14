import itertools
import operator
import math
from functools import reduce

def compute(verbose=False):
    # Observation: probability of getting n reds is sum of product of every size-n subset
    #   of [1, N], divided by (N+1)!
    N = 15 # NUM TURNS
    total = 0
    for i in range(1+(N-1)//2):
        for numbers in itertools.combinations(range(1,N+1), i):
            total += reduce(operator.mul, numbers, 1)

    answer = int(math.factorial(N+1)/total)
    return answer, 'Highest profitable payout for game'
