import operator
import utils
import bisect

def compute(verbose=False):
    MAX = 10**11
    MAX = MAX // 2
    PRIMES_1MOD4 = [p for p in utils.get_first_primes(3*(10**6)) if p%4==1]

    def get_mults(limit):
        results = []
        for i in range(1, limit+1):
            f = utils.prime_factorize(i)
            is_valid = True
            for prime in f:
                if prime%4==1:
                    is_valid = False
            if is_valid:
                results.append(i)
        return results

    def make_cumulative_list(a):
        result = []
        total = 0
        for elt in a:
            total += elt
            result.append(total)
        return result

    MULTS = sorted(get_mults(140000))
    MULTS_SUM = make_cumulative_list(MULTS)

    def sum_below(limit): # Calculate sum of all elements in MULTS that are <= limit
        i = bisect.bisect(MULTS, limit)
        return i
        return MULTS_SUM[i-1]

    def get_base_solutions(powers, so_far=[]):
        if len(powers) == len(so_far):
            return [so_far] # Base case
        results = []
        new_power = powers[len(so_far)]
        prod_so_far = 1
        for i in range(len(so_far)):
            prod_so_far *= so_far[i]**powers[i]
        limit = (MAX / prod_so_far)**(1/new_power)
        for pi in range(len(PRIMES_1MOD4)):
            prime = PRIMES_1MOD4[pi]
            if prime in so_far:
                continue # Don't re-use a prime
            if prime > limit:
                break # Can't go bigger
            results.extend(get_base_solutions(powers, so_far + [prime]))
        return results

    answer = 0
    for powers in [(3,2,1), (7,3), (10,2)]:
        base_sols = get_base_solutions(powers)
        for base_sol in base_sols:
            num = 1
            for i in range(len(powers)):
                num *= (base_sol[i]**powers[i])
            limit = MAX//num
            answer += sum_below(limit)
            #answer += 2*(num * sum_below(limit))
    return answer, 'In progress'  # Right now I'm finding number of solutions, and it's off by almost EXACTLY a factor of 2. Weird
