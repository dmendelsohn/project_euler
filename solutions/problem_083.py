import search
import utils

# Another minimum path cost problem through a matrix, all directions are allowed
def compute(verbose=False):  # Straight up dijkstra (astar with no heuristic)
	text_lines = open(utils.INPUT_PATH + 'p083_matrix.txt').read().strip().split('\n')
	MATRIX = [list(map(int, line.split(','))) for line in text_lines]
	N = len(MATRIX)
	def cost_func(vertex1, vertex2): # Cost of moving from vertex1 to vertex2 in graph
		(row, col) = vertex2
		cost = MATRIX[row][col]
		if vertex1 == (0,0): # Have to add initial cost as well
			cost += MATRIX[0][0]
		return cost
	def move_func(vertex): # Possible moves from vertex
		(row, col) = vertex
		moves = [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]
		return filter(lambda move: 0 <= move[0] < N and 0 <= move[1] < N, moves)
	path = search.astar((0,0), (N-1,N-1), cost_func, move_func)
	answer = search.cost_of_path(path, cost_func)
	return answer, "Sum of minimum top-left to bottom-right path"
