import itertools
import utils

# Compute largest square formed by an anagramic pair
def compute():  # We generally treat words as list of ints 0...25
	# Return tuple of 26 elements, representing the counts of a...z respectively
	def get_frequency_dist(word):
		count = [0]*26
		for c in word:
			count[c] += 1
		return tuple(count)

	# Returns a dict mapping a frequency distribution to list of words with that distribution
	def get_anagrams(words):
		anagrams = {}
		for w in words:
			dist = get_frequency_dist(w)
			anagrams[dist] = anagrams.get(dist, []) + [w]
		return anagrams

	# Return dict mapping letters (0...25) to digits, or None if no mapping exists
	def get_mapping(word, num):  # Assumes num has same number of digits as word as letters
		digits = utils.get_digits(num, reverse=True)
		available = set(range(10))
		mapping = {}
		for i in range(len(word)):
			letter = word[i]
			if letter in mapping: # Already have a mapping for this letter
				if mapping[letter] != digits[i]: # We have a mapping conflict
					return None
			elif digits[i] not in available: # New required digit has already been used
				return None
			else:
				mapping[word[i]] = digits[i]
				available.remove(digits[i])
		return mapping

	def apply_mapping(word, mapping):
		digits = list(map(lambda letter: mapping[letter], word))
		return utils.make_number(digits, reverse=True)

	# Return highest square in an a-b anagram pair, or 0 if a and b cannot be an anagram pair
	# Assume word1 and word2 are anagrams and all squares are correct number of digits
	def best_anagram_square(word1, word2, squares):
		best = 0
		for sq in squares:
			mapping = get_mapping(word1, sq)
			if mapping: # If there is a valid mapping
				num = apply_mapping(word2, mapping) 
				if num in squares:
					best = max(best, sq, num)
		return best

	words = open(utils.INPUT_PATH + 'p098_words.txt').read().split(',')
	words = map(lambda s: s.strip('\"'), words)  # Strip quotation marks
	# Make each word a list of integers, 0 for A, 25 for Z
	words = [list(map(lambda c: ord(c) - ord('A'), w)) for w in words]
	anagrams = get_anagrams(words)

	# FIlter out anagram sets of 1 element
	anagrams = {dist:anagrams[dist] for dist in anagrams if len(anagrams[dist]) > 1}

	# Make dict mapping integer lengths to set of squares of that length
	max_length = max(map(sum, anagrams.keys()))
	squares = {i:set() for i in range(max_length+1)}
	for i in range(1,utils.isqrt(10**max_length)):
		sq = i**2
		squares[utils.num_digits(sq)].add(sq)

	best = 0
	for dist in anagrams:
		for (a,b) in itertools.combinations(anagrams[dist], 2):
			best = max(best, best_anagram_square(a, b, squares[sum(dist)]))
	return best, 'Highest square in anagram pair'
