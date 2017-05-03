import utils

# How many L < 1.5 million are sum of EXACTLY ONE Pythagorean triple
def compute(verbose=False):
    MAX_NUM = 1500000
    MEMO = {} # maps L to how many triples (so far) sum to it
    for m in range(1, utils.isqrt(MAX_NUM)):
        for n in range(1, m):
        	if utils.gcd(m,n) != 1 or (m*n)%2==1:
        		continue # Not a primitive triple
        	base_perim = 2*m*(m+n)
        	L = base_perim
        	while L < MAX_NUM:  # Account for multiples of primitive triples with L small enough
        		MEMO[L] = 1 + MEMO.get(L,0)
        		L += base_perim
    answer = sum(MEMO[L] == 1 for L in MEMO)
    return answer, "Number of L < 1.5million that are the sum of exactly one Pythagorean triple"
