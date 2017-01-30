import utils

# Compute sum of perimeters of all almost equilateral triangles with integer area and perimeter < 10^9
# Using Heron's formula, we can figure out that we need (3s+-1)(s-+1) to be a perfect square, where s is the repeated side
# After some rearranging we can restate the problem:
# For all x of the form 2^a * k^2, where a > 0 and k odd, Let x-1, x-1, x-2 or x+1, x+1, x+2 be the sides
# ... area will be integer iff x * perimeter is square
def compute():
	MAX = 10**9
	total_perimeter = 0 # Total perimeter
	max_k = utils.isqrt(MAX//6)
	for k in range(1, max_k+1, 2):  # Consider all odd k whose squares are small enough
		x = 2 * (k**2)
		while x <= MAX//3:
			for y in (3*x+4, 3*x-4):
				if utils.is_square(x*y) and 3 <= y <= MAX:  # y < 3 is degenerate triangle
					total_perimeter += y
			x *= 2
	text = 'Sum of perimeters of almost equilateral triangles with integer area'
	return total_perimeter, text

