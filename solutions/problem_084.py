import random


# Compute the most three most likely squares in monopoly if 4-sided dice are used
# Warning!  This is probabilistic and may yield wrong answer (but it's not too likely)
def compute(verbose=False):
    GO, JAIL, G2J = 0, 10, 30
    RR = [5,15,25,35]  # Railroads
    U = [12,28] # Utilities
    CC = [2,17,33] # Community chest
    CH = [7,22,36] # Chance
    CC_DEST = [GO, JAIL]
    CH_DEST = [GO, JAIL, 11, 24, 39, 5]
    def next_space(spaces, pos): # Return next space in sorted spaces list greater than pos
        i = 0
        while i < len(spaces) and spaces[i] <= pos:
        	i += 1
        i %= len(spaces) # Wrap around if needed
        return spaces[i]
    def cc_result(x, pos): # x should be in range(16), pos in range(40)
        if x < 2:  # fixed destinations
        	return CC_DEST[x]
        else:  #  No movement
        	return pos
    def ch_result(x, pos): # x should be in range(16), pos in range(40)
        if x < 6: # fixed destinations
        	return CH_DEST[x]
        elif x < 8:  # next RR
        	return next_space(RR, pos)
        elif x == 8: # next U
        	return next_space(U, pos)
        elif x == 9:  # Go back three spaces
        	return pos-3
        else: # No movement
        	return pos
    def get_roll(n): # 2 dice, n sides per die
        return (random.randint(1,n), random.randint(1,n))
    freq = [0]*40  # Frequency counter
    ch_cards, cc_cards = list(range(16)), list(range(16))
    random.shuffle(ch_cards)
    random.shuffle(cc_cards)
    ch_index, cc_index = 0, 0
    pos = 0  # Initial position
    num_doubles = 0 # No initial doubles
    for i in range(10**5): # Number of rolls to simulate
        freq[pos] += 1 # Update frequency count before moving on
        roll = get_roll(4)
        if roll[0] == roll[1]:  # Handle counting doubles
        	num_doubles += 1
        else:
        	num_doubles = 0
        pos = (pos + roll[0] + roll[1])%40  # New position, pending potential changes
        if num_doubles == 3 or pos == G2J:  # 3 doubles in a row OR go to jail, same result
        	pos = JAIL
        	num_doubles = 0
        elif pos in CC:  # Community chest
        	pos = cc_result(cc_cards[cc_index], pos)  # Do whatever it says
        	cc_index = (cc_index+1)%16  # Next time, draw next card
        elif pos in CH:  # Chance
        	pos = ch_result(ch_cards[ch_index], pos)  # Do whatever it says
        	ch_index = (ch_index+1)%16 # Next time, draw next card
    most_frequent = sorted(enumerate(freq), key=lambda x: x[1], reverse=True)
    most_frequent = [x[0] for x in most_frequent[:3]]
    a = most_frequent[0]*10000 + most_frequent[1]*100 + most_frequent[2]  # concatenate numbers
    return a, 'Concatenated digits for three most frequent monopoly squares'
