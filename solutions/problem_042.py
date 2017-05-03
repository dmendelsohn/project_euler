import utils

# Compute number of words in the file whose numerical score is a triangle number
def compute(verbose=False):
	def word_score(word):
		return sum(ord(c)-64 for c in word)
	tri_nums = {n*(n+1)/2 for n in range(1,100)}
	words = open(utils.INPUT_PATH + "p042_words.txt").read().replace("\"","").split(",")
	return sum(word_score(w) in tri_nums for w in words), "Number of triangle words"
