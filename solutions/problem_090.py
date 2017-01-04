import operator
import itertools

# How many distinct pairs of dice can generate all squares between 01 and 81?  6 and 9 are distinct but can be used interchangeably
def compute():
	targets = [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(8,1)] # Recall 6==9, which simplifies things
	def num_solutions((a,b)): # Check if all targets can be made by dice (6-tuples) a, b
		return reduce(operator.and_, (((t1 in a and t2 in b) or (t1 in b and t2 in a)) for (t1,t2) in targets), True)
	def simplify_die(die):  # Returns die as a set, with 9 replaced with 6 if there is one
		die = set(die)
		if 9 in die:  # 
			die.remove(9)
			die.add(6)
		return die
	dice = map(simplify_die, itertools.combinations(range(10),6))  # 0-8, because 9 is equiv to 6
	sols = filter(num_solutions, itertools.combinations(dice,2))
	return len(sols), 'Number of dice sets that can generate all squares'
