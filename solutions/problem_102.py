import math
import utils

# How many of the triangles contain the origin?
def compute(verbose=False):
	ABC = [-340, 495, -153,-910, 835, -947]
	XYZ = [-175,41, -421,-714, 574,-645]
	# Gets list of 'arcs' between vectors to points in triangle, in radians
	def contains_origin(tri): # tri is list of 6 ints (x1 y1 x2 y2 x3 y3)
		angles = sorted(math.atan2(tri[2*i+1], tri[2*i]) for i in range(3)) # Angles is sorted list of vectors to the points
		arcs = [(angles[i]-angles[i-1])%(2*math.pi) for i in range(3)] # Gaps between those vectors
		return max(arcs) < (math.pi - 0.000001) # If maximum arc is strictly less than pi, origin is inside triangle
	lines = open(utils.INPUT_PATH + 'p102_triangles.txt').read().strip().split('\n')
	triangles = map(lambda line: map(int, line.split(',')), lines)  # Triangle is now list of ints
	answer = len(filter(contains_origin, triangles))
	return answer, 'Number of triangles containing the origin'
