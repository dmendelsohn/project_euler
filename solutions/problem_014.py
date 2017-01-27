# What number < one million produces the longest Collatz chain?
def compute():
	MEMO = {}
	def collatz(n):
		if n in MEMO:
			pass #just return memo[n], no need to update table
		elif n == 1:
			MEMO[n] = 1  # Base case
		elif n%2==0:
			MEMO[n] = 1+collatz(n/2)
		else:
			MEMO[n] = 1+collatz(3*n+1)
		return MEMO[n]
	length, start = max((collatz(i), i) for i in range(1, 10**6+1))
	return start , "The number under one million that produces longest Collatz chain (%d)" % (length,)
