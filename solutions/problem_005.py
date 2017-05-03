import utils

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def compute(verbose=False):
    lcm = {}  # Lcm will keep track of how many times we need each prime
    for n in range(1, 21):
        fact = utils.prime_factorize(n)
        for (prime, num_times) in fact.items():
        	lcm[prime] = max(lcm.get(prime, 0), num_times) # Update count for this prime
    num = 1 # Reconstruct number whose prime factorization is lcm
    for (prime, num_times) in lcm.items():
        num *= (prime ** num_times)
    return num, "The smallest positive number that is evenly divisible by 1, 2, ..., 20"
