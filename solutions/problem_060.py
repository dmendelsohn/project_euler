import itertools
import utils

# Find smallest number that's sum of 5 primes, s.t. all pairwise concatenations of those 5 is also prime
# Observation: 5 primes must all be equivalent mod 3 (except 3 itself is always fine)
# WARNING: Long-ish runtime (40s)
def compute(verbose=False):
	MAX_NUM = 10**8
	PRIMES = utils.get_first_primes(MAX_NUM, as_set=True)
	if verbose:
		print("There are %d reference primes under %d" % (len(PRIMES), MAX_NUM))
	def concat(x,y):
		return x * (10**utils.num_digits(y)) + y
	def is_prime(x):
		if x < MAX_NUM:
			return x in PRIMES
		else:
			return utils.is_prime(x)
	def is_edge(x,y):
		return is_prime(concat(x,y)) and is_prime(concat(y,x))
	def is_valid_expansion(clique, vertex, edges):
		if vertex <= clique[-1]:
			return False
		for v in clique:
			if (v, vertex) not in edges:
				return False
		return True
	base_primes = utils.get_first_primes(8400, as_set=False) # Would really have to do 25250 to verify
	if verbose:
		print("There are %d base primes" % (len(base_primes),))
	primes = [[p for p in base_primes if (p%3==j or p==3)] for j in range(1,3)] # Sort into two buckets, 3 goes in both
	cliques = {i: set() for i in range(2,6)} # 2-cliques just edges
	if verbose:
		n, m = len(primes[0]),len(primes[1])
		poss_edges = (n**2-n + m**2 - m)//2
		print("There are %d possible edges" % (poss_edges,))
	count = 0
	for i in range(2):
		for (p1, p2) in itertools.combinations(primes[i], 2): # For all pairs of primes
			count += 1
			if count%(10**4)==0:
				if verbose:
					#print("...%d possible edges checked" % (count,))
					pass
			if is_edge(p1, p2):
				cliques[2].add((p1,p2))  # Min comes first in pair
	if verbose:
		print("There are %d edges" % (len(cliques[2]),))
	for i in range(2,5): #Build 2->3, 3->4, 4->5 cliques
		for c in cliques[i]: # Shall we expand this clique?
			for new_prime in primes[c[-1]%3-1]: #Only iterate over useful primes
				if is_valid_expansion(c, new_prime, cliques[2]):
					cliques[i+1].add((c+(new_prime,)))
		if verbose:
			print("There are %d %d-cliques" % (len(cliques[i+1]), i+1))
	if verbose:
		print("5-cliques: %s" % (str(cliques[5]),))
	if cliques[5]:
		return min(map(sum, cliques[5])), "Minimum sum of 5-clique"
	else:
		return -1, 'No solution found'
