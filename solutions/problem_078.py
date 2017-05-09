import fast

# Smallest n for which p(n) is divisible by one million (p is partition function)
def compute(verbose=False):
    # MEMO = [-1]*60000 # Only need this many, by trial and error
    # MEMO[0] = 1 # By definition, p(0)=1
    # def pentagonal(k):
    #     return k*(3*k-1)//2
    # def p(n):  # Partition function, calculated using recurrence relation I found on Wikipedia
    #     count = 0
    #     k = 1
    #     pent = pentagonal(k)
    #     while pent <= n:
    #     	if k%2==1:
    #     		count += MEMO[n-pent]
    #     	else:
    #     		count -= MEMO[n-pent]
    #     	k = -k
    #     	if k > 0:
    #     		k += 1
    #     	pent = pentagonal(k)
    #     return count%10**6  # We only care about modulo 10**6
    # n = 1
    # while True:
    #     MEMO[n] = p(n)
    #     if MEMO[n]==0:
    #     	return n, "Lowest number for which p(n) | 10^6"
    #     	return
    #     n += 1
    n = fast.p78_helper()
    return n, "Lowest number for which p(n) | 10^6"
