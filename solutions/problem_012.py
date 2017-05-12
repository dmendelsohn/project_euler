import utils
import fast

# What is the value of the first triangle number to have over five hundred divisors?  Solution is 12375th triangle #...OPTIMIZE
def compute(verbose=False):
    n = 1
    fact = utils.prime_factorize(n)
    while True:
        next_fact = utils.prime_factorize(n+1)
        prod_fact = utils.multiply_factorizations(fact, next_fact)
        prod_fact[2] -= 1 # Divide by 2
        if (utils.count_divisors(prod_fact) > 500):
            return n*(n+1)//2, "First triangle number with over 500 divisors"
        n += 1
        fact = next_fact

if __name__ == "__main__":
    print(compute())
