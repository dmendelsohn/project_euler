import utils

# What is first value that can be written as sum of primes in > 5000 different ways?
def compute(verbose=False):
	MEMO = {}
	MAX = 10**3
	PRIMES = utils.get_first_primes(MAX, as_set=False)
	def count_prime_partitions(n,k):
		k = min(n,k)
		if n == 0:
			return 1
		elif n == 1:
			return 0  # No way to do it
		elif (n,k) in MEMO:
			return MEMO[(n,k)]
		else:
			i, count = 0, 0
			while PRIMES[i] <= k:  # PRIMES[i] is next prime to use
				count += count_prime_partitions(n-PRIMES[i],PRIMES[i])
				i += 1
			MEMO[(n,k)] = count
			return count
	n = 1
	while count_prime_partitions(n,n-1) <= 5000 and n < MAX:
		n += 1
	if n == MAX:
		return -1, "Need to make MAX bigger than %d" % (MAX,)
	else:
		return n, "Smallest number that can be written as sum of primes in > 5000 ways"
