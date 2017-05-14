# Compute least n for which number of ways to fill n-unit strip with red bars of length at least 50
# and black unit squares, such that no two red bars are adjacent exceeds 10**6
def compute(verbose=False):
    THRESH = 10**6
    M = 50
    MEMO = [(0,1)] # MEMO[n][0] is ways for n-length strip ending with red, MEMO[n][1] with black
    n = 1
    while True: # Build MEMO[n]
        red = MEMO[-1][0] # Extend last red bar on any n-1,red solution by 1 unit
        if n >= M:
            red += MEMO[-M][1] # Add new length-M red on any n-3,black solution
        black = MEMO[-1][0] + MEMO[-1][1] # Add black onto any n-1 solution
        MEMO.append((red,black))
        num_sols = red+black
        if num_sols > THRESH:
            break
        n += 1
    return n, 'Least n for which number of solutions exceeds {}'.format(THRESH)