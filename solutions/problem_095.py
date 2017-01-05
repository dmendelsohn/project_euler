import utils

# Consider all looping chains by iteratively taking sum of proper divisors of a number.  What is the
# minimum element in the longest chain that has no value exceeding one million?
def compute():
	MAX = 1+10**6
	sigmas = utils.get_first_sigmas(MAX)
	for i in range(len(sigmas)):
		sigmas[i] -= i  # We only care about proper divisors
	seen = set()
	longest_chain = set()
	for i in range(1, MAX):
		chain = []
		index = 0
		while i not in seen and i < MAX:
			seen.add(i)
			chain.append(i)
			i = sigmas[i]
		if i in chain: # checks that we looped
			chain = chain[chain.index(i):] # Cut off the part that's not part of the loop
			if len(chain) > len(longest_chain):
				longest_chain = chain
	return min(longest_chain), 'Minimum element in longest "sum of proper divisors" chain'