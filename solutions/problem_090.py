import operator
import itertools

# How many distinct pairs of dice can generate all squares between 01 and 81?  6 and 9 are distinct but can be used interchangeably
def compute(verbose=False):
    targets = [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(8,1)] # Recall 6==9, which simplifies things
    def is_solution(die1, die2): # Check if all targets can be made by dice (6-tuples)
        is_sol = True # Initially assume true, change to false if we can't create any target
        for (tens, ones) in targets:
        	if not ((tens in die1 and ones in die2) or (tens in die2 and ones in die1)):
        		is_sol = False
        return is_sol
    def simplify_die(die):  # Returns die as a set, with 9 replaced with 6 if there is one
        die = set(die)
        if 9 in die:  # 
        	die.remove(9)
        	die.add(6)
        return die
    dice = map(simplify_die, itertools.combinations(range(10),6))  # 0-8, because 9 is equiv to 6
    num_sols = 0
    for (die1, die2) in itertools.combinations(dice, 2):
        if is_solution(die1, die2):
        	num_sols += 1
    return num_sols, 'Number of dice sets that can generate all squares'
