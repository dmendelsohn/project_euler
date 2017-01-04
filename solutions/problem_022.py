import utils

# Compute sum of scores for each name in list
def compute():
	def get_name_score(name):
		return sum(map(lambda c: ord(c)-64, name))
	names = sorted(open(utils.INPUT_PATH+'p022_names.txt').read().replace('\"',"").split(','))
	answer = sum((i+1)*get_name_score(names[i]) for i in range(len(names)))
	return answer, "Sum of scores of all names in the list"
