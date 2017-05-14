# Compute number of ways to fill 50-unit strip with red bars of length at least 3
# and black unit squares, such that no two red bars are adjacent
def compute(verbose=False):
    LEN = 50
    MEMO = [(0,1)] # MEMO[n][0] is ways for n-length strip ending with red, MEMO[n][1] with black
    for n in range(1,LEN+1): # Build MEMO[n]
        red = MEMO[-1][0] # Extend last red bar on any n-1,red solution by 1 unit
        if n >= 3:
            red += MEMO[-3][1] # Add new length-3 red on any n-3,black solution
        black = MEMO[-1][0] + MEMO[-1][1] # Add black onto any n-1 solution
        MEMO.append((red,black))
    answer = MEMO[LEN][0] + MEMO[LEN][1]
    return answer, 'Number of ways to fill 50-unit strip, according to the rules'