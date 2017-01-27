# Find cyclic sequence of 6 4-digit numbers, including each of polygonal numbers from 3-8
def compute():
	POLY = {}
	for n in range(3,9):
		ngonals = set()
		num, inc = 1, 1
		while num < 10**4:
			if num >= 10**3:
				ngonals.add(num)
			inc += n-2
			num += inc
		POLY[n] = ngonals

	def get_next(possible_n, start_digits=None, end_digits=None):
		results = []
		for n in possible_n:
			for num in POLY[n]:
				if start_digits != None and num//100 != start_digits:
					continue  # This number is out
				if end_digits != None and num%100 != end_digits:
					continue # This number is out
				results.append((num, n))
		return results
	def get_sols(list_so_far, remaining_n):
		if len(remaining_n) == 0:
			return sum(list_so_far) # List containing a single solution (which is a list)
		start_digits, end_digits = None, None
		if len(list_so_far) > 0:
			start_digits = list_so_far[-1]%100
		if len(remaining_n) == 1:
			end_digits = list_so_far[0]//100 # Make sure it wraps around 
		next_moves = get_next(remaining_n, start_digits, end_digits)
		for (num, n) in next_moves:
			remaining_n.remove(n)
			x = get_sols(list_so_far + [num], remaining_n)
			if x:
				return x # We're done!
			remaining_n.add(n)
		return 0 # No solution found

	return get_sols([],set(range(3,9))), "The sum of the first solution set"
