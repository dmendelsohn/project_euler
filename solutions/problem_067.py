import utils

# Just compute the continuous path from top of triangle to bottom with highest sum (same as Problem #18)
def compute():
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
	grid = utils.load_grid(utils.INPUT_PATH + "p067_triangle.txt", ' ')
	answer = max(best_to_point(grid,len(grid)-1,j) for j in range(len(grid)))
	return answer, "Maximum sum through triangle"
