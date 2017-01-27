import utils

# What p <= 1000 is the sum of the most Pythagorean triples?
def compute():
	MEMO = {}  # Perimiter : # Pythagorean triples with that perimeter
	for a in range(1,334):
		for b in range(a, (1000-a)//2):
			c = utils.isqrt(a**2 + b**2)
			p = a + b + c
			if a**2 + b**2 == c**2 and p <= 1000:  # Check if this is a Pythagorean triple, and is small enough
				MEMO[p] = MEMO.get(p,0)+1
	ans = max(MEMO, key=MEMO.get)
	return ans, 'Number <= 1000 that is sum of the most Pythagorean triples (%d triples)' % (MEMO[ans])
