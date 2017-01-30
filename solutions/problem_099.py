import math
import utils

# Determine which of the given a^b values is biggest
def compute():
	text = open(utils.INPUT_PATH + 'p099_base_exp.txt').read().split('\n')
	pairs = map(lambda line: list(map(int, line.split(','))), text)
	logs = list(map(lambda pair: pair[1]*math.log(pair[0]), pairs))  # Get log_2 of each a^b
	best_index = logs.index(max(logs)) + 1
	return best_index, 'Line number of largest a^b pair in file'
