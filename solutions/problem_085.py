import utils

# Compute area of grid with as close as possible to 2 million rectangles
# Observation: mxn rectangle as T_m * T_n rectangles within, where T_i is the ith Triangle number
# If 'MAX' were bigger, might want to do some sort of binary search for b based on a.  Not necessary now.
def compute():
	MAX = 2*10**6
	TRI = [n*(n+1)/2 for n in range(utils.isqrt(2*MAX))]
	a, b = 1, len(TRI)-1
	best, area = 0, 0
	for a in range(1,len(TRI)):
		b = a
		while b < len(TRI) and a*TRI[b-1] < MAX:
			count = TRI[a]*TRI[b]
			if abs(MAX-count) < abs(MAX-best):
				best, area = count, a*b
			b+=1
	return area, 'Area of grid with as close as possible to two million rectangles'
