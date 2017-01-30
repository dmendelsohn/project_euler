import itertools

# Solve the sudokus and sum the three digits top-left number in each
def compute():
	def print_puzzle(puzzle):
		s = ''
		for r in range(9):
			for c in range(9):
				s += str(puzzle[(r,c)])
			s += '\n'
		print(s)
	def get_row_locs(r):
		return [(r, i) for i in range(9)]
	def get_col_locs(c):
		return [(i, c) for i in range(9)]
	def get_box_locs(loc): # Get box locations for box containing (r,c)
		(r,c) = loc
		(r,c) = (r-r%3, c-c%3) # (r,c) is now top left corner of the box
		return [(r+rd,c+cd) for (rd,cd) in itertools.product(range(3),repeat=2)]
	def possible_moves(puzzle): # Returns grid, where each element is set of allowed digits
		grid = {(r,c):set(range(1,10)) for (r,c) in itertools.product(range(9),repeat=2)}
		# For eah spot in the puzzle, constrain all related spots
		for (r,c) in itertools.product(range(9),repeat=2):
			val = puzzle[(r,c)]
			if val == 0: # This is an empty square and doesn't constrain other squares
				continue # So we do nothing
			grid[(r,c)] = set() # No possible moves for already filled in space
			locs = set(get_row_locs(r) + get_col_locs(c) + get_box_locs((r,c)))
			for loc in locs:
				grid[loc].discard(val)
		return grid

	def possible_moves_by_loc(puzzle, loc):  # Returns set of possible moves for a single location
		(r,c) = loc
		if puzzle[(r,c)] != 0:
			return set() # This space is already filled in, no possible moves
		possible = set(range(1,10))
		for loc in set(get_row_locs(r) + get_col_locs(c) + get_box_locs((r,c))):
			possible.discard(puzzle[loc])
		return possible

	# If any square has only one possibility, fill it in, return number of moves made
	def apply_deduced_moves(puzzle, possible_moves):
		count = 0
		for loc in possible_moves: # dictionary with (r,c) keys and set values
			if len(possible_moves[loc]) == 1:
				puzzle[loc] = list(possible_moves[loc])[0]

	# Figure out if any number only has one possible placement in the group
	def apply_group_deduction(puzzle, group, possible_moves): 
		# Group is list of locations (could be row, col or box)
		for i in range(9):  # For each digit 1-9
			possible_placements = [loc for loc in group if i in possible_moves[loc]]
			if len(possible_placements) == 1:  # If the digit can only go in one place
				puzzle[possible_placements[0]] = i # place it

	# Solve via backtracking, in recursive calls, specify loc_index. Return True if successful
	def backtrack(puzzle, loc_index=-1):
		loc_index += 1
		if loc_index == 9*9: # We got to the end and filled everything in!  We're done
			return True
		loc = (loc_index//9, loc_index%9)  # loc_index is index in flattened grid
		if puzzle[loc] != 0:
			return backtrack(puzzle, loc_index)  # Just keep going
		possible = possible_moves_by_loc(puzzle, loc)
		for digit in possible:
			puzzle[loc] = digit
			if backtrack(puzzle, loc_index):  # True iff puzzle was solved with assumptions so far
				return True # We're done
			puzzle[loc] = 0 # Reset to empty
		return False # We failed

	def solve_sudoku(puzzle): # Represented as 9x9 list of lists of digits, with blanks = 0
		# First solve by deduction
		last_puzzle = None
		while puzzle != last_puzzle:
			last_puzzle = puzzle.copy()
			possible = possible_moves(puzzle)
			apply_deduced_moves(puzzle, possible)  # If a space can only have one fill, fill it
			groups = [] # List of list of locs
			for i in range(9):
				groups.append(get_row_locs(i))
				groups.append(get_col_locs(i))
			for loc in itertools.product(range(0,9,3),repeat=2):
				groups.append(get_box_locs(loc))
			for g in groups:
				# If a number can only go in one place in a group, place it
				apply_group_deduction(puzzle, g, possible)
		backtrack(puzzle)  # Finish the rest of the puzzle via brute-force backtracking
		return puzzle

	def parse_input(): # Returns a list of 50 sudokus
		puzzles = [None]*50
		text = open('inputs/p096_sudoku.txt').read().split('\n')
		for i in range(50):
			subtext = text[10*i+1:10*i+10]
			puzzles[i] = {}
			for (r,c) in itertools.product(range(9), repeat=2):
				puzzles[i][(r,c)] = int(subtext[r][c])
		return puzzles
	puzzles = parse_input()
	puzzles = map(solve_sudoku, puzzles)
	puzzles = filter(lambda p: 0 not in p.values(), puzzles)
	nums = map(lambda p: 100*p[(0,0)] + 10*p[(0,1)] + p[(0,2)], puzzles)
	return sum(nums), 'Sum of top left corner of solved sudokus'
