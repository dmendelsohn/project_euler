import utils

# Find the smallest cube for which exactly five permutations of its digits are cube.
def compute():
	MAX_BASE = 10**4
	MEMO = {} # Keys: tuple of digits from lowest to highest
	cubes = [x**3 for x in range(MAX_BASE)]
	for c in cubes:  # Build memo of digits to list of cubes with those digits
		digits = utils.get_sorted_digits(c)
		MEMO[digits] = MEMO.get(digits, []) + [c]
	ans = min(map(min, (MEMO[d] for d in MEMO if len(MEMO[d]) == 5))) # Minimum element in a value list (if the value list has length 5)
	return ans, 'Smallest cube for which exactly five permutations of its digits are cubes'
