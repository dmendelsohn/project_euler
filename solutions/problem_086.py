import utils


# Least value of M for which there are at least 1,000,000 integral routes
# Observation: For a 'new' solution (cube's max dimension = M), we need a Pythagorean
# triple with a side of length M (and we count how many ways to divide the other side)
# In dividing the other side, recall that the order of the partition does not matter
def compute():
	MAX = 10**4 # Maximum M, tuned down by trial and error
	new_sols = {}  # key i is count of how many new solutions m=i is (compared to m=i-1)
	triangles = [] # This will be (a,b) for all Pythagorean triples that may contribute solutions
	for n in range(1, utils.isqrt(MAX)): # We generate all unique Pythagorean triples small enough to matter
		for m in range(n+1, MAX//n):
			if utils.gcd(n,m) != 1 or (m*n)%2==1:  # Check if not coprime, or both odd
				continue # We want m,n for primitive primes only, so we skip
			for k in range(1, MAX//(m*n)):
				triangles.append((k*(m**2-n**2), 2*k*m*n))
	for (a,b) in triangles:  # Process the triangles, tracking how many new solutions each adds
		a, b = min(a,b), max(a,b)  # Make sure a is lower
		new_sols[a] = new_sols.get(a, 0) + max(0,a+1-(b+1)//2)  # Short side is M, divide up the other (if we can)
		new_sols[b] = new_sols.get(b, 0) + a//2 # Long side is M, divide up the other
	count, i = 0, 0	# Find lowest index where cumulative sum exceeds threshold
	while i < MAX and count < 10**6:
		count += new_sols.get(i, 0)
		i += 1
	return i-1, 'Least M with at least one million solutions'
