import utils
import fast

# When we iteratively do (sum of factorial of digits), how many n < 10^6 yield 
# a chain of exactly 60 non-repeating terms?
def compute(verbose=False):
    # Brute force
    # FACTS = utils.get_first_factorials(10)
    # MEMO = {1:1, 2:1, 145:1, 40585:1, 871:2, 45361:2, 
    #     	872:2, 45362:2, 169:3, 363601:3, 1454:3} # Manually enumerate loops
    # def iterate(x):
    #     return sum([FACTS[d] for d in utils.get_digits(x)])
    # def update_chain(x):  # Assumes we will get to an existing loop
    #     chain = []
    #     while x not in MEMO:
    #     	chain.append(x)
    #     	x = iterate(x)
    #     base_num = MEMO[x]
    #     for i in range(len(chain)):
    #     	MEMO[chain[i]] = base_num + len(chain) - i
    # count = 0
    # for i in range(1, 10**6):
    #     if i not in MEMO:
    #     	update_chain(i)
    #     if MEMO[i] == 60:
    #     	count += 1
    count = fast.p74_helper()
    return count, 'Number of n < one million that yield length-60 chain'
