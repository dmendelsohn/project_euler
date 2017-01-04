import utils

# Smallest sum path through matrix
def compute():
	MEMO = {}
	MATRIX = [map(int, l.split(',')) for l in open(utils.INPUT_PATH + 'p081_matrix.txt').read().strip().split('\n')]
	N = len(MATRIX)
	def get_partial_min(r, c): # Get min to row r, col c
		if r < 0 or c < 0:
			return None
		elif (r,c) in MEMO:
			return MEMO[(r,c)]
		else:
			m = MATRIX[r][c]
			a, b = get_partial_min(r-1,c), get_partial_min(r, c-1)  # Possible paths to get here, or None
			vals = [v for v in (a,b) if v != None] # Filter out the ones that are None
			if vals: # If there are non-None paths (i.e. we're not just beginning)
				m += min(vals)
			MEMO[(r,c)] = m
			return m
	return get_partial_min(N-1, N-1), "Sum of minimum path"
