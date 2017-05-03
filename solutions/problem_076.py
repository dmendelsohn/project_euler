# How many ways can 100 be written as sum of at least 2 positive integers?  (Permuting is NOT unique)
def compute(verbose=False):
	MAX = 100
	MEMO = {(i, 1): 1 for i in range(1, MAX+1)}
	def count_partitions(n,k):  # Number of ways to sum to n with integers at most k
		k = min(n,k)  # k > n is useless
		if n == 0:
			return 1 # Empty set is the one way
		elif (n,k) in MEMO:
			return MEMO[(n,k)]
		else:
			count = sum(count_partitions(n-i,i) for i in range(1,k+1))
			MEMO[(n,k)] = count
			return count
	answer = count_partitions(MAX, MAX-1) # Don't want to count trivial one-element partition
	return answer, "Number of partitions of %d" % (MAX,)
