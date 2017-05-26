import fast

#@profile
def compute(verbose=False):
    # Calculate number of cubes in nth layer, base cuboid has surface area
    # S and total edge length E
    # Num cubes in layer = S + (l-1)*E + (l-1)*(l-2)*4

    return fast.p126_helper(limit=20000,target=1000) # Empirically found limit

