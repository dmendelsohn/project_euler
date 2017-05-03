import utils

# Smallest sum path through matrix
def compute(verbose=False):
    MEMO = {}
    text_lines = open(utils.INPUT_PATH + 'p081_matrix.txt').read().strip().split('\n')
    MATRIX = [list(map(int, line.split(','))) for line in text_lines]
    N = len(MATRIX)
    def get_partial_min(row, col): # Get min to row r, col c
        if row < 0 or col < 0:
        	return None
        elif (row, col) in MEMO:
        	return MEMO[(row, col)]
        else:
        	val = MATRIX[row][col]
        	# Compute two candidate minimum path sums
        	sum1, sum2 = get_partial_min(row-1,col), get_partial_min(row, col-1)
        	sums = [v for v in (sum1, sum2) if v != None] # Filter out the ones that are None
        	if sums: # If there are non-None paths (i.e. we're not just beginning)
        		val += min(sums)
        	MEMO[(row, col)] = val
        	return val
    return get_partial_min(N-1, N-1), "Sum of minimum path"
