import itertools
import operator
import utils

# For a set of digits, we can combine them with any operation to reach many targets.
# Find set of digits with ability to reach all 1...n for the highest n
def compute(verbose=False):
    OPS = [(operator.add, False), (operator.sub, False), (operator.sub, True), \
        (operator.mul, False), (operator.truediv, False), (operator.truediv, True)]
    MEMO = {} # Maps sorted tuples of digits to set of reachable values
    MEMO[tuple()] = set() # Empty tuple of digits can reach the empty set of values
    for i in range(10): # 
         MEMO[(i,)] = set([i]) # A single digit can only reach itself
    def get_possible_values(digits):
        if digits in MEMO:
            return MEMO[digits]
        possible = set()
        for subset in utils.powerset(digits[1:]):
            left = (digits[0],)+subset
            if len(left) == len(digits):
                continue # Skip this, to avoid infinite recursion
            right = tuple(sorted(set(digits)-set(left)))
            left_vals = get_possible_values(left)
            right_vals = get_possible_values(right)
            for (left_val, right_val, op) in itertools.product(left_vals, right_vals, OPS):
                if op[1]: # Reverse if necessary
                    left_val, right_val = right_val, left_val
                try:
                    new_val = op[0](left_val, right_val)
                    possible.add(new_val)
                except ZeroDivisionError:
                    continue # Just move on
        MEMO[digits] = possible
        return possible

    best = 0, () # Lowest_impossible, digits tuple
    for digits in itertools.combinations(range(10), 4):
        possible = get_possible_values(digits)
        n = 1
        while n in possible:
            n +=1 # Eventually n will be lowest impossible number
        if n > best[0]:
            best = (n, digits)
    ans = utils.concatenate_ints(best[1])
    text = 'Four digits that allow for highest range of reachable values (up to %d)' % (best[0]-1,)
    return ans, text

if __name__ == "__main__":
    print(compute())
