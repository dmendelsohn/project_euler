import itertools
import utils

# Integer points (x1, y1), (x2, y2); 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed (together with (0,0))
def compute():
	def count_sols(x,y): # Count right triangles with right angle at (x,y), x, y > 0 and another vertex at (0,0)
		(n,d) = utils.simplify_frac(y,x) # Simplified slope m
		return min((50-y)/d, x/n) + min(y/d, (50-x)/n)  # Number of points that fit on line with -1/m slope through (x,y)
	a = sum(count_sols(x,y) for (x,y) in itertools.product(range(1,51),repeat=2))
	a += 3*50*50  # Add 50*50 solutions for each of: right angle on x=0, right angle on y=0: right angle at origin
	return a, 'Number of right triangles'
