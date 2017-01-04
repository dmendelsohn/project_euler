import utils
import operator

def compute():
	def answer(grid, step, num=4):  # Assume grid is well-formed, step is (row, col)
		R, C, best = len(grid), len(grid[0]), 0
		for r in range(R):
			for c in range(C):
				if 0 <= r + step[0]*(num-1) < R and 0 <= c + step[1]*(num-1) < C:
					best = max(best, reduce(operator.mul, (grid[r+step[0]*i][c+step[1]*i] for i in range(num))))
		return best
	grid = utils.load_grid(utils.INPUT_PATH + 'p011_grid.txt', ' ')
	a = max([answer(grid, s) for s in [(1, 1), (1, -1), (1, 0), (0, 1)]])
	return a, "Largest product of four consecutive numbers in the grid"
