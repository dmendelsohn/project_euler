import search
import utils

# Another minimum path cost problem through a matrix, movement right, up, down is allowed
def compute(): # Strategy: add 'start' and 'end' states to each side, other states will all be (r,c) tuples
	MATRIX = [map(int, l.split(',')) for l in open(utils.INPUT_PATH + 'p082_matrix.txt').read().strip().split('\n')]
	N = len(MATRIX)
	def cost_func(v1, v2): # Cost of moving from v1 to v2 in graph
		if v2 == 'end':
			return 0  # No cost to move to 'end' state from right side
		else: # v2 should be of (r,c) form
			(r,c) = v2
			return MATRIX[r][c]
	def move_func(v): # Possible moves from v
		if v == 'start':
			return [(r,0) for r in range(N)]  # Entire left-most column
		elif v == 'end':
			return [] # No moves from end
		(r,c) = v # Normal (r,c) state
		if c == N-1:
			return ['end'] # We're on the right side, no need to move anywhere but the end state
		else:  # Normal (r,c) state
			moves = [(r,c+1), (r+1,c), (r-1,c)]
			return filter(lambda (r,c): 0 <= r < N and 0 <= c < N, moves)
	path = search.astar('start', 'end', cost_func, move_func)
	answer = search.cost_of_path(path, cost_func)
	return answer, "Sum of minimum left-to-right path"
