import utils

# Just calculate 40 choose 20 (it's a path counting problem)
def compute(verbose=False):
	return utils.nCr(40,20), "Number of paths"
