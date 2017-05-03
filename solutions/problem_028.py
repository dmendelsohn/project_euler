# Get sum of diagonals of 1001x1001 spiral square
def compute(verbose=False):
	return 1 + sum((4*n*n - 6*n + 6) for n in range(3, 1002, 2)), "Sum of diagonals"
