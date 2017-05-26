import utils

# Compute sum of palindromic numbers < 10**8 that can be expressed as sum of consecutive squares
# Note: Formula for sum of first n squares is n(n+1)(2n+1)/6
def compute(verbose=False):
    MAX = 10**8

    def sum_of_squares(n):
        return n*(n+1)*(2*n+1)//6

    max_sq = utils.isqrt(MAX)
    possible = set()
    for i in range(max_sq+1):
        for j in range(i+2, max_sq+1):
            sum_i_j = sum_of_squares(j) - sum_of_squares(i)
            if sum_i_j < MAX:
                if utils.is_palindrome(sum_i_j):
                    possible.add(sum_i_j)
            else:
                break # Move on to next i
    ans = sum(possible)
    return ans, 'Sum of palindromic nums < 10**8 that are sum of consecutive squares'
