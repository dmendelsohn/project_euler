import utils

# How many unique reduced proper fractions are there with d <= 10^6
def compute(verbose=False):
	MAX_DEN = 10**6
	phis = utils.get_first_totients(MAX_DEN+1)  # When totients are numerator, we have proper fractions
	answer = sum(phis[2:])
	return answer, "Number of unique proper fractions with denominators <= one million"
