import random
import numpy as np
import scipy.sparse.linalg as sla

# Compute the most three most likely squares in monopoly if 4-sided dice are used
def compute(verbose=False): 
    N = 4
    SIZE = 40
    GO, JAIL, G2J = 0, 10, 30
    RR = [5,15,25,35]  # Railroads
    U = [12,28] # Utilities
    CC = [2,17,33] # Community chest
    CH = [7,22,36] # Chance
    CC_DEST = [JAIL, GO]
    CH_DEST = [JAIL, GO, 11, 24, 39, 5]

    def get_rolls():
        rolls = {} #  maps (num, is_double) -> probability
        for i in range(2, 2*N+1): # Initialize ignoring doubles
            rolls[(i,False)] =  (N-abs(N+1-i))/(N**2) 
            rolls[(i,True)] = 0
        for i in range(2,2*N+1,2): # account for doubles
            rolls[(i, True)] += 1/(N**2)
            rolls[(i, False)] -= 1/(N**2)
        return rolls

    def next_space(spaces, pos): # Return next space in sorted spaces list greater than pos
        i = 0
        while i < len(spaces) and spaces[i] <= pos:
            i += 1
        i %= len(spaces) # Wrap around if needed
        return spaces[i]

    # Be careful to call CH before CC, because it's possible for a CH to send you to a CC loc
    def transfer_columns(A, is_CH): # Category should be 
        if is_CH:
            locs = CH
        else:
            locs = CC

        for loc in locs:
            for num_dubs in range(3):
                col = num_dubs*SIZE + loc

                # Calculate destination columns
                if is_CH:
                    next_rr_loc = next_space(RR, loc)
                    next_util_loc = next_space(U, loc)
                    dest_locs = CH_DEST + [next_rr_loc, next_rr_loc, next_util_loc, (loc-3)%40]
                else:
                    dest_locs = CC_DEST

                for dest_loc in dest_locs:
                    #dest_col = dest_loc + (num_dubs*SIZE if dest_loc != JAIL else 0) # Reset doubles count
                    dest_col = dest_loc + (num_dubs*SIZE) # Don't reset doubles count
                    A[:,dest_col] += A[:,col]/16
                A[:,col] *= (16-len(dest_locs))/16

    # Row i represents transition from pos i%40 with i//40 doubles, columns are transition to that state
    A = np.zeros((3*SIZE,3*SIZE))
    rolls = get_rolls()

    # Account for initial transitions (regular rolling, accounting for doubles sending to jail)
    for row in range(3*SIZE):
        (loc, num_dubs) = row%40, row//40
        for (move, is_double) in rolls:
            next_loc = (loc+move)%SIZE
            next_num_dubs = (num_dubs+1 if is_double else 0)
            if next_num_dubs < 3: # No need to go to jail, regular situation
                A[row][next_num_dubs*SIZE + next_loc] += rolls[(move, is_double)]
            else: # Go to jail due to 3 doubles, reset doubles count to 0
                A[row][JAIL] += rolls[(move, is_double)]

    # Do transfers away from Chance (CH) and Community Chest (CC) columns
    transfer_columns(A, is_CH=True)
    transfer_columns(A, is_CH=False)
   
    # Transfer all of G2J columns to JAIL
    for num_dubs in range(3):
        #A[:,JAIL] += A[:,num_dubs*SIZE + G2J]  # Reset doubles count
        A[:,num_dubs*SIZE + JAIL] += A[:,num_dubs*SIZE + G2J]  #  Don't reset doubles count
        A[:,num_dubs*SIZE + G2J] = 0


    # Find normalized left eigenvector with eigenvalue 1
    eigvals, eigvecs = sla.eigs(A.transpose()) # TODO: confirm 5th eigenvalue is 1
    j = -1 # Index of relevant eigval
    for i in range(len(eigvals)):
        if abs(eigvals[i]-1) < 10**-6:
            j = i
            break
    if j == -1:
        return -1, "No eigenvalue of 1 in transition matrix"

    stable = -eigvecs[:,j] # v is left eigenvector corresponding to value 1
    stable /= sum(stable) # normalize v

    # Extract answer
    results = stable[0:SIZE] + stable[SIZE:2*SIZE] + stable[2*SIZE:3*SIZE] # Collapse num_doubles together
    results = enumerate(results)
    results = sorted(results, key=lambda r: r[1], reverse=True)

    if verbose:
        print("Squares ranked by frequency:")
        for r in results:
            print("Square {}: {:.3f}%".format(r[0],100*r[1].real))

    a = results[0][0]*(10**4) + results[1][0]*(10**2) + results[2][0]
    return a, 'Concatenated digits for three most frequent monopoly squares'

# Warning!  This is probabilistic and may yield wrong answer 
def compute_monte_carlo(verbose=False):
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

if __name__ == "__main__":
    print(compute(True))

