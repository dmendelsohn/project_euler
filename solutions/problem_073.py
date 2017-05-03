import utils

# How many fractions lie strictly between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?
def compute(verbose=False):
    MAX_DEN = 12000
    count = 0
    for den in range(2,MAX_DEN+1):
        for num in range(1 + (den//3), (den+1) // 2):  # These enforce the bounds
        	if utils.gcd(den, num) == 1: # Check if n/d is proper
        		count += 1
    text = "Number of proper fractions between 1/3 and 1/2 with denominators <= %d" % (MAX_DEN,)
    return count, text
