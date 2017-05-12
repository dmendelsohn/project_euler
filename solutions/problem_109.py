import itertools

# Find number of ways to checkout in darts with a score less than 100
def compute(verbose=False):
    N = 100
    MOVES = list(itertools.product(range(1,21), range(1,4)))
    MOVES.extend([(25, 1), (25, 2)])
    count = 0
    for double_out_val in list(range(1,21))+[25]:
        priors = list(itertools.combinations_with_replacement(MOVES, 2)) # Two-dart priors
        priors += list(map(lambda m: (m,), MOVES)) # One-dart priors, wrap all moves as a singleton-tuple
        priors += [()] # Add empty tuple representing zero-dart prior
        for prior_darts in priors:
            value = double_out_val*2
            for dart in prior_darts:
                value += dart[0]*dart[1]
            if value < N:
                count += 1
    return count, 'Number of ways to checkout in darts with a score under {}'.format(N)