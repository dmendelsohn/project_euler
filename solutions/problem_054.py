import utils

# How many poker hands does player 1 win?
def compute():
	RANKS = '0123456789TJQKA'
	VALUES = {RANKS[i]:i for i in range(len(RANKS))}
	HIGH, PAIR, TWO_PAIR, THREE_KIND, STRAIGHT, FLUSH, FULL_HOUSE, FOUR_KIND, STRAIGHT_FLUSH = tuple(range(9))
	def is_straight(cards): # returns high value or None
		ranks = set(c[0] for c in cards)
		return len(ranks) == 5 and max(ranks) - min(ranks) == 4  # Five different ranks, with max and min 4 apart
	def is_flush(cards): # returns suit or None
		suits = set(c[1] for c in cards)
		return len(suits) == 1
	def get_groups(cards): # returns {group_size: list of ranks}, group_size in 0...4
		freq_count = {}
		for c in cards: # Calculate frequency counts
			freq_count[c[0]] = freq_count.get(c[0],0)+1
		groups = {i:[] for i in range(1,5)}
		for rank in freq_count:  # Load up group dictionary
			groups[freq_count[rank]].append(rank)
		for count in groups: # Sort each group
			groups[count].sort(reverse=True)
		return groups
	def process_hand(cards): #Input is list of strings like '5C', #Output of the form [score, tiebreakers...]
		cards = [(VALUES[c[0]], c[1]) for c in cards] # Cards are now (int, str)
		s = is_straight(cards)
		f = is_flush(cards)
		groups = get_groups(cards)
		if s and f:
			result = STRAIGHT_FLUSH
		elif s:
			result = STRAIGHT
		elif f:
			result = FLUSH
		elif groups[4]:
			result = FOUR_KIND
		elif groups[3]:
			if groups[2]:
				result = FULL_HOUSE
			else:
				result = THREE_KIND
		elif groups[2]:
			if len(groups[2]) == 2:
				result = TWO_PAIR
			else:
				result = PAIR
		else:
			result = HIGH
		return [result] + groups[4] + groups[3] + groups[2] + groups[1]
	hands = open(utils.INPUT_PATH + 'p054_poker.txt', 'rt').read().strip().split('\n')
	count = 0 # Count or P1 wins
	for hand in hands:
		cards = hand.strip().split()
		p1_cards, p2_cards = cards[:5], cards[5:] # list of cards, each with str repr
		p1_result, p2_result = process_hand(p1_cards), process_hand(p2_cards)
		if p1_result > p2_result:
			count += 1
	return count, 'Number of hands won by Player 1'
