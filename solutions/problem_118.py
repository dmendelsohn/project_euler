import itertools
import utils

#TODO: description
def compute(verbose=False):
    def get_num_sets(minimum, digits):
        n = len(digits)
        if n == 0:
            return 1 # Base case
        min_length = utils.num_digits(minimum)
        lengths = [i for i in range(1,1+n//2) if min_length <= i <= 8]
        if min_length <= n <= 8:
            lengths.append(n)
        num_sols = 0
        for length in lengths:
            for next_digits in itertools.permutations(digits, length):
                num = utils.make_number(next_digits)
                if num > minimum and utils.is_prime(num):
                    remaining_digits = digits - set(next_digits)
                    num_sols += get_num_sets(num, remaining_digits)
        return num_sols

    digits = set(range(1,10))
    answer = get_num_sets(1, digits)
    return answer, 'Number of pandigital prime sets'
