import utils

# Compute maximum sum down the triangle
def compute(verbose=False):
    MEMO = {}
    def best_to_point(grid, i, j):
        if (i,j) in MEMO:
        	return MEMO[(i,j)]
        elif (j > i) or (i < 0) or (j < 0):
        	return 0
        else:
        	a = best_to_point(grid, i-1, j)
        	b = best_to_point(grid, i-1, j-1)
        	answer = grid[i][j] + max(a,b)
        	MEMO[(i,j)] = answer
        	return answer
    grid = utils.load_grid(utils.INPUT_PATH + "p018_triangle.txt", ' ')
    a = max(best_to_point(grid,len(grid)-1,j) for j in range(len(grid)))
    return a, "Maximum sum"
