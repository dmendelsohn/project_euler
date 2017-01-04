# Print a*b*c where a,b,c are a Pythagorean triple with sum 1000
def compute():
	for m in range(15,24):
		for n in range(1, m):
			if 2*m*(m+n) == 1000:
				a, b, c = m*m-n*n, 2*m*n, m*m+n*n
				return a*b*c, "The product of the unique Pythagorean triple with sum 1000 (%d, %d, %d)" % (a,b,c)
	return -1, "No answer found"