import search
import utils

# Another minimum path cost problem through a matrix, all directions are allowed
def compute():  # Straight up dijkstra (astar with no heuristic)
	MATRIX = [map(int, l.split(',')) for l in open(utils.INPUT_PATH + 'p083_matrix.txt').read().strip().split('\n')]
	N = len(MATRIX)
	def cost_func(v1, v2): # Cost of moving from v1 to v2 in graph
		(r,c) = v2
		cost = MATRIX[r][c]
		if v1 == (0,0): # Have to add initial cost as well
			cost += MATRIX[0][0]
		return cost
	def move_func(v): # Possible moves from v
		(r,c) = v
		moves = [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]
		return filter(lambda (r,c): 0 <= r < N and 0 <= c < N, moves)
	path = search.astar((0,0), (N-1,N-1), cost_func, move_func)
	answer = search.cost_of_path(path, cost_func)
	return answer, "Sum of minimum top-left to bottom-right path"
