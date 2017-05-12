import utils

# https://artofproblemsolving.com/wiki/index.php?title=1996_AIME_Problems/Problem_8
# The link above helped me figure out that the number of solutions is just (N+1)//2,
# where N is the number of factors of n^2

# Find lowest n where number of unique solutions to 1/x + 1/y = 1/n is over 1000
# By note above, find lowest n where number of factors is at least 2002
def compute(verbose=False):
    N = 4*10**6
    # Reasonable safe estimates for maximum multiplicity of each prime in factorization of n
    PRIMES = [(2, 5), (3, 4), (5, 3), (7, 3), (11, 3), (13, 3), (17, 2), (19, 2), (23, 1), (29, 1), (31, 1), (37, 1)]
    def get_all_factorizations(remaining_primes, max_power):
        if not remaining_primes or max_power == 0: # Base case
            return [{}] # List containing just the empty dict
        max_power = min(max_power, remaining_primes[0][1])
        new_prime = remaining_primes[0][0]
        results = []
        for power in range(max_power+1): # Consider new_prime**power in factorization
            for fact in get_all_factorizations(remaining_primes[1:], power):
                fact[new_prime] = power
                results.append(fact)
        return results

    def eval_factors(d):
        result = 1
        for prime in d:
            result *= (prime**d[prime])
        return result

    possible = []
    for n_factors in get_all_factorizations(PRIMES, PRIMES[0][1]):
        squared = {prime: n_factors[prime]*2 for prime in n_factors}
        num_sols = (utils.count_divisors(squared)+1)//2
        if num_sols > N:
            possible.append(n_factors)

    # Evaluate all factorization dicts in possible, and take min
    answer = min(map(eval_factors, possible))
    return answer, 'Lowest n where 1/x + 1/y = 1/n has over {} integer solutions'.format(N)