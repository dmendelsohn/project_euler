import utils

# Compute number of numbers under 50 million that are prime1^2 + prime2^3 + prime3^4
def compute(verbose=False):
	MAX = 5*10**7
	PRIMES = utils.get_first_primes(utils.isqrt(MAX)+2000) # Get some buffer on the end
	quad_max = int(MAX**0.25)
	trip_max = int(MAX**(1.0/3))
	dub_max = int(MAX**0.5)
	results = set()
	i = 0
	while PRIMES[i] <= quad_max:
		j = 0
		while PRIMES[j] <= trip_max: # Can make slight improvement skipping some third powers
			k = 0
			while PRIMES[k] <= dub_max: # Can make slight improvement skipping some squares
				s = PRIMES[i]**4 + PRIMES[j]**3 + PRIMES[k]**2
				if s < MAX:
					results.add(s)
				k += 1
			j += 1
		i += 1
	return len(results), 'Number of integers under 50 million that are sum of square,cube,and fourth power of primes'
