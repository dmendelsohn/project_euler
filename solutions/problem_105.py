import itertools
import utils

def compute(verbose=False):
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

    sets = utils.load_grid(utils.INPUT_PATH + "p105_sets.txt", ",")
    sets = list(map(sorted, sets))  # Now each is sorted
    answer = sum(map(sum, filter(is_special_sum_set, sets)))
    return answer, "Sum of sums of all special sum sets in text file"