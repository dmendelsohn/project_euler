import utils

# Find the first four consecutive integers to have four distinct prime factors each
def compute():
	MAX = 10**6  # Find by trial and error
	sieve = [0 for i in range(MAX)]  # Initialize array
	for prime in utils.get_first_primes(MAX//(2*3*5)):  # Bigger prime factors won't help
		mult = 1
		while (prime*mult < MAX):
			sieve[prime*mult] += 1
			mult += 1
	i = 1
	while (sieve[i:i+4].count(4) != 4):
		i += 1
	return i, 'Start of smallest four consecutive integers to have four distinct prime factors each'
