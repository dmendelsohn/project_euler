import utils
import operator
from functools import reduce

# Compute highest product of 'line' of four elements in grid
def compute():
	# Compute highest product of line in a specific direction, specified by 'step'
	def answer(grid, step, num=4):  # Assume grid is well-formed, step is (row_delta, col_delta)
		num_rows, num_cols, best = len(grid), len(grid[0]), 0
		for row in range(num_rows):
			for col in range(num_cols):
				if 0 <= row + step[0]*(num-1) < num_rows and 0 <= col + step[1]*(num-1) < num_cols:
					product = 1
					for i in range(num):
						product *= grid[row+step[0]*i][col+step[1]*i]
					best = max(best, product)
		return best
	grid = utils.load_grid(utils.INPUT_PATH + 'p011_grid.txt', ' ')
	a = max([answer(grid, step) for step in [(1, 1), (1, -1), (1, 0), (0, 1)]])
	return a, "Largest product of four consecutive numbers in the grid"
