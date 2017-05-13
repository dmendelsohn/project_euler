import itertools
import utils

# M(k, d) is the greatest number, m, for which there exists a k-digit number with m repeats
#   of the digit d
# N(k, d) is the number of k-digit primes with M(k,d) repeats of the digit d
# S(k, d) is the sum of all k-digit primes with M(k,d) repeated of the digit d
# Compute sum(S(10,d) for d in range(10)
def compute(verbose=False):
    NUM_DIGITS = 10
    ALL_ONES = [0]
    for i in range(1, 11):
        ALL_ONES.append(ALL_ONES[-1]*10+1)
    def get_primes(num_digits, repeated_digit, num_repeats):
        other_digits = set(range(10)) - set([repeated_digit])
        num_other_digits = num_digits - num_repeats
        other_digit_sets = itertools.product(other_digits, repeat=num_other_digits)
        results = []
        other_digit_positions = itertools.combinations(range(num_digits), num_other_digits)
        for digits, positions in itertools.product(other_digit_sets, other_digit_positions):
            num = ALL_ONES[num_digits]*repeated_digit # Starting point
            for (digit, position) in zip(digits, positions):
                num += (digit-repeated_digit)*(10**position)
                if utils.is_prime(num):
                    if num >= 10**(num_digits-1): # Get rid of results with leading 0s
                        results.append(num)
        return results
    def calc_M_N_S(num_digits, repeated_digit):
        # Try successively smaller m until we have results
        for m in range(num_digits-1, -1, -1):  # m ought not get non-positive anyway, but just in case
            results = get_primes(num_digits, repeated_digit, m)
            if len(results) > 0:
                return (m, len(results), sum(results))

    total = 0
    for i in range(10):
        m, n, s = calc_M_N_S(NUM_DIGITS, i)
        total += s
    return total, 'Sum of S(10, d) for d in range(10)'
