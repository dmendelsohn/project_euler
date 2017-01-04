import utils

# Find smallest spiral where diagonals are < 10% prime
def compute():
	prime_count, diag_count = 0, 1
	n = 3
	while True:
		prime_count += [utils.is_prime(n*n - (n-1)*i) for i in range(4)].count(True)
		if (prime_count * 10 < 2*n-1):
			return n, 'Smallest square for which diagonal of spiral is < 0.1 prime'
		n += 2
