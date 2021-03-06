import itertools

# How many distinct terms are in the sequence generated by ab for 2 <= a <= 100 and 2 <= b <= 100?
def compute(verbose=False):
    return len(set(i**j for (i,j) in itertools.product(range(2,101), repeat=2))), "Number of distint terms"
