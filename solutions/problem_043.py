import itertools
import utils

# Find the sum of all 0 to 9 pandigital numbers with this property. (See description)
def compute():
	MODS = [2, 3, 5, 7, 11, 13, 17]
	def has_property(x): #assumes 0-9 pandigital
		for i in range(len(MODS)):
			if ((x/10**(6-i))%1000)%MODS[i] != 0:
				return False
		return True
	perms = [utils.make_number(d) for d in itertools.permutations(range(10), 10)]
	return sum(filter(has_property, perms)), 'Number of 0-9 pandigital numbers with the property'
