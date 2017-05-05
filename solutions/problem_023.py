import fast
import itertools
import utils

# Add all numbers that can't be written as sum of two abundant numbers
def compute(verbose=False):  # Kinda slow
    MAX=28123  # Thanks, math!
    sigmas = utils.get_first_sigmas(MAX)
    abundant_nums = [i for i in range(MAX) if 2*i < sigmas[i]]
    possible = fast.p23_get_possible_sums(abundant_nums, MAX)
    #possible = set(i+j for (i,j) in itertools.combinations_with_replacement(abundant_nums, 2)) # Slow
    total = sum(i for i in range(1, MAX) if i not in possible)
    return total, "Sum of all numbers that cannot be written as sum of two abundant numbers"

if __name__ == "__main__":
    print(compute())
