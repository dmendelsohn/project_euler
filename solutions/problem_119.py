import utils

# Find the 30th number that is a power of the sum of its digits (a sum needs at least two digits)
def compute(verbose=False):
    results = set()
    for base in range(1,200):  # Empirically found to be big enough base
        for power in range(1,20): # Empirically found to be big enough power
            num = base**power
            if num >= 10 and utils.sum_of_digits(num) == base:
                results.add(num)
    results = list(sorted(results))
    if len(results) >= 30:
        return results[29], '30th number that is a power of the sum of its digits'
    else:
        return -1, 'No answer found'
