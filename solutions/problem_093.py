import itertools
import operator
import utils

from fractions import Fraction

# For a set of digits, we can combine them with any operation to reach many targets.
# Find set of digits with ability to reach all 1...n for the highest n
# Warning: Runtime ~ 22s

# Solved by finding all reachable numbers for a given set of digits by making all possible
# evaluation trees
def compute():
	# An op is an operator and a boolean, which is whether to reverse, i.e. do (right op left)
	OPS = [(operator.add, False), (operator.sub, False), (operator.sub, True), \
		(operator.mul, False), (operator.truediv, False), (operator.truediv, True)]

	# Represent computations option as tree: leaves are int, non-leaves are operations 
	# on their child subtrees
	def generate_trees(digits):  # digits is a set or a tuple of digits
		digits = set(digits) # Cast to set
		if len(digits) == 0:
			return [] # No solutions
		if len(digits) == 1:
			return [list(digits)[0]] # Trivial solution, just a leave of the tree
		# Map each subset of digits to list of possible subtrees
		# Be sure to skip the 'full' subset or we get infinite recursion
		subtrees = {frozenset(subset):generate_trees(subset) \
			for subset in utils.powerset(digits) if len(subset) != len(digits)} 
		results = []
		# Iterate through subsets containing smallest elt
		for subset in filter(lambda s: min(digits) in s, subtrees.keys()):
			subset = frozenset(subset) # Need hashable sets, frozenset works
			complement = frozenset(digits - subset)
			for (left, right) in itertools.product(subtrees[subset], subtrees[complement]):
				results.extend([(op, left, right) for op in OPS])
		return results

	# Tree is either an int, or a tuple of the form ((op, reverse), left_tree, right_tree)
	# Return Fraction if evaluation is possible, or else None
	def evaluate(tree):  # Use rational numbers, because intermediate result need not be integers
		if isinstance(tree, int):
			return Fraction(tree)
		(op, reverse), left, right = tree
		if reverse:
			left, right = right, left
		try:
			return op(evaluate(left), evaluate(right))
		except: # Divide by zero error somewhere down the line
			return None

	# Return the first unreachable target for a given set of digits
	def lowest_impossible(digits):
		values = set(evaluate(tree) for tree in generate_trees(digits))
		values = set(int(v) for v in values if v != None and v > 0 and v.denominator == 1)
		n = 1
		while n in values:
			n+=1
		return n

	best = max((lowest_impossible(digits), digits) 
				for digits in itertools.combinations(range(10), 4))
	ans = utils.concatenate_ints(sorted(best[1]))
	text = 'Four digits that allow for highest range of reachable values (up to %d)' % (best[0]-1,)
	return ans, text
