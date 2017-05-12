import utils

# https://artofproblemsolving.com/wiki/index.php?title=1996_AIME_Problems/Problem_8
# The link above helped me figure out that the number of solutions is just (N+1)//2,
# where N is the number of factors of n^2

# Find lowest n where number of unique solutions to 1/x + 1/y = 1/n is over 1000
# By note above, find lowest n where number of factors is at least 2002
def compute(verbose=False):
    N = 1000
    INC = 2*3*5*7*11 # Shortcut: hypothesize n has the lowest primes as factors
    n = INC
    while (utils.num_divisors(n**2)+1)//2 <= N:
        n += INC
    return n, 'Lowest n where 1/x + 1/y = 1/n has over {} integer solutions'.format(N)