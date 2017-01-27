import search
import utils

# Another minimum path cost problem through a matrix, movement right, up, down is allowed
def compute(): # Strategy: add 'start' and 'end' states to each side, other states will all be (r,c) tuples
	text_lines = open(utils.INPUT_PATH + 'p082_matrix.txt').read().strip().split('\n')
	MATRIX = [list(map(int, l.split(','))) for l in text_lines]
	N = len(MATRIX)
	def cost_func(vertex1, vertex2): # Cost of moving from vertex vertex1 to vertex2 in graph
		if vertex2 == 'end':
			return 0  # No cost to move to 'end' state from right side
		else: # vertex2 should be of (row, col) form
			(row, col) = vertex2
			return MATRIX[row][col]
	def move_func(vertex): # Possible moves from vertex
		if vertex == 'start':
			return [(row,0) for row in range(N)]  # Entire left-most column
		elif vertex == 'end':
			return [] # No moves from end
		(row, col) = vertex # Normal (row, col) state
		if col == N-1:
			return ['end'] # We're on the right side, no need to move anywhere but the end state
		else:  # Normal (row, col) state
			moves = [(row, col+1), (row+1, col), (row-1, col)]
			return filter(lambda move: 0 <= move[0] < N and 0 <= move[1] < N, moves)
	path = search.astar('start', 'end', cost_func, move_func)
	answer = search.cost_of_path(path, cost_func)
	return answer, "Sum of minimum left-to-right path"
