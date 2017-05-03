import utils

# Compute area of grid with as close as possible to 2 million rectangles
# Observation: mxn rectangle as T_m * T_n rectangles within, where T_i is the ith Triangle number
# If 'MAX' were bigger, might want to do some sort of binary search for b based on a.  Not necessary now.
def compute(verbose=False):
	MAX = 2*10**6
	TRI = [n*(n+1)/2 for n in range(utils.isqrt(2*MAX))]
	best, area = 0, 0
	for i in range(1,len(TRI)):
		j = i
		while j < len(TRI) and i*TRI[j-1] < MAX:
			count = TRI[i]*TRI[j]
			if abs(MAX-count) < abs(MAX-best):
				best, area = count, i*j
			j+=1
	return area, 'Area of grid with as close as possible to two million rectangles'
