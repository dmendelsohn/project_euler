import utils

# Find number of non-bouncy numbers below 10^100
# A non-bouncy number has digits that are either increasing or decreasing
def compute(verbose=True):
    POW = 100
    increasing = utils.nCr(POW+9,9) # 10 buckets: [0,1,2,3,4,5,6,7,8,9], 100 elts
    increasing -= 1 # Don't count 0
    decreasing = utils.nCr(POW+10,10) # 11 buckets: [0,9,8,7,6,5,4,3,2,1,0], 100 elts
    decreasing -= (POW+1) # Discount all 0's (all breakdowns between leading and trailing)
    answer = increasing + decreasing
    answer -= POW*9  # So we don't double count numbers that are both increasing and decreasing
    return answer, 'Number of non-bouncy numbers below 10^{}'.format(POW)
