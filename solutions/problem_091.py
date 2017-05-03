import itertools
import utils

# Integer points (x1, y1), (x2, y2); 0 <= x1, y1, x2, y2 <= 50,
# how many right triangles can be formed (together with (0,0))
def compute(verbose=False):
    # Count right triangles with right angle at (x,y), where x,y > 0 and another vertex at (0,0)
    def count_sols(x,y):
        (num, den) = utils.simplify_frac(y,x) # Simplified slope m
        # Return number of points that fit on line with slope -1/m through (x,y)
        return min((50-y)//den, x//num) + min(y//den, (50-x)//num)
    num_sols = sum(count_sols(x,y) for (x,y) in itertools.product(range(1,51),repeat=2))
    # Add 50*50 for each of the other cases for right angle: (on x=0), (on y=0), (at origin)
    num_sols += 3*50*50
    return num_sols, 'Number of right triangles'
