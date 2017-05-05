import fast

# What number < one million produces the longest Collatz chain?
#@profile
def compute(verbose=False):
    MAX = 10**6
    return fast.p14_helper(MAX) 
    
    # MEMO = {}
    # def collatz(n):
    #     if n in MEMO:
    #     	pass #just return memo[n], no need to update table
    #     elif n == 1:
    #     	MEMO[n] = 1  # Base case
    #     elif n%2==0:
    #     	MEMO[n] = 1+collatz(n>>1)
    #     else:
    #     	MEMO[n] = 1+collatz(3*n+1)
    #     return MEMO[n]
    # length, start = max((collatz(i), i) for i in range(1, MAX+1))
    # return start , "The number under one million that produces longest Collatz chain (%d)" % (length,)

if __name__ == "__main__":
    print(compute())
