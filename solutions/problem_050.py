import utils

# Which prime, below one-million, can be written as the sum of the most consecutive primes?
def compute(verbose=False):
    primes = utils.get_first_primes(10**6)
    d = set(primes)
    best = 0
    for length in range(2,10**3): # maximum by trial and error
        start = 0
        window = sum(primes[start:start+length])
        while window < 10**6:
        	if window in d:
        		best = window
        	window += primes[start+length] - primes[start] # This *shouldn't* go out of bounds
        	start += 1
    return best, 'The prime below one million that can be written as the sum of the most consecutive primes'
