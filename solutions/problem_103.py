import itertools
import utils

def compute(verbose=False):
    def is_sorted_and_unique(t):
        for i in range(len(t)-1):
            if t[i] >= t[i+1]:
                return False
        return True

    def is_special_sum_set(t): # t is sorted iterable
        # Cond 2: Check that smallest size-{i+1} subset has bigger sum that biggest size-i subset
        for i in range(1, (len(t)+1)//2):
            if sum(t[:i+1]) <= sum(t[:len(t)-i-1:-1]):
                return False

        # Cond 1: Make sure no subsets have same sum
        # Observation: due to cond 2, only need to check subset pairs that are same size
        for i in range(2, 1+len(t)//2): 
            sums = set()
            for subset in itertools.combinations(t, i):
                if sum(subset) in sums:
                    return False
                sums.add(sum(subset))
        return True # Both conditions hold
        
    APPROX = (20,31,38,39,40,42,45)
    k = 2 # Assume that each elt of solution is within k of approximate solution (it turns out it's within 0)
    best_t = APPROX
    best_sum = sum(best_t)
    for delta in itertools.product(range(-k,k+1), repeat=7):
        t = tuple(sum(x) for x in zip(APPROX, delta))
        if sum(t) < best_sum and is_sorted_and_unique(t) and is_special_sum_set(t):
            best_t, best_sum = t, sum(t)
            print(t)

    answer = utils.concatenate_ints(best_t)
    return answer, "Set-string for optimal special sum set for n=7"
