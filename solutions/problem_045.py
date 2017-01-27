# Find the smallest tri/pent/hex number > T285 = P165 = H143 = 40755.
def compute():
	MAX = 10**5  # Trial and error to reduce this
	MEMO = {} # Maps number to 1,2,3 (count of how many of tri/pent/hex it is)
	for n in range(1, MAX):
		tri = n*(n+1)//2
		MEMO[tri] = MEMO.get(tri,0) + 1
		pent = n*(3*n-1)//2
		MEMO[pent] = MEMO.get(pent,0) + 1
		hexa = n*(2*n-1)
		MEMO[hexa] = MEMO.get(hexa,0) + 1
	answer = [n for n in MEMO if MEMO[n] == 3][2]
	return answer, 'Next triagonal/pentagonal/hexagonal number after 40755'
