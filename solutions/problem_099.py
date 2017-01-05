import math
import utils

# Determine which of the given a^b values is biggest
def compute():
	text = open(utils.INPUT_PATH + 'p099_base_exp.txt').read().split('\n')
	pairs = map(lambda line: map(int, line.split(',')), text)
	logs = map(lambda (a,b): b*math.log(a), pairs)  # Now we have log_2 of each a^b
	best_index = logs.index(max(logs)) + 1
	return best_index, 'Line number of largest a^b pair in file'