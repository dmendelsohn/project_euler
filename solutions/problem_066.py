import math
import utils

# Find D in [2,1000] for which mininum solution (in x) for x^2 - D*y^2 = 1 is highest
def compute():
	def rationalize(num, (a, b, c)):  # Takes in fraction of form num / (a*sqrt(b)+c)
		num = (num*a, b, -num*c)
		den = a*a*b - c*c
		return (num, den)
	def divide(num, g):  # num could be int for 3-tuple
		if isinstance(num, int):
			return num/g
		else: # it's a 3-tuple
			return (num[0]/g, num[1], num[2]/g)
	def simplify(num, den):
		numbers = []
		for x in [num, den]:
			if isinstance(x, int):
				numbers.append(x)
			else: # It's a 3-tuple
				numbers.append(x[0])
				numbers.append(x[2])
		g = reduce(utils.gcd, numbers)
		return divide(num,g), divide(den,g)
	def floor((a,b,c), den):
		return int((a*math.sqrt(b)+c)/den)
	def next_step(num, (a,b,c)): # (num/(a*sqrt(b)+c) is current state
		(a, b, c), den = rationalize(num, (a,b,c))
		s = floor((a,b,c), den)
		c -= s*den
		num, den = simplify((a,b,c), den)  # num is 3-tuple
		return (s, den, num)
	def init_step(x):
		s = utils.isqrt(x)
		return (s,1,(1,x,-s))
	def is_sol(x,y,D):
		return x*x-D*y*y==1
	def get_min_x_sol(D):  # Using Pell equation
		h = {-2: 0, -1: 1} #Initialize h sequence
		k = {-2: 1, -1: 0} #Initialize k sequence
		a = []
		step = init_step(D)
		n = 0
		while True:
			a.append(step[0])
			h[n] = a[n]*h[n-1] + h[n-2]
			k[n] = a[n]*k[n-1] + k[n-2]
			if is_sol(h[n],k[n],D):
				return h[n]
			n += 1
			step = next_step(step[1],step[2]) # next_step(num, (a,b,c))
	worst = 0, None  #(x, D)
	for D in range(2, 1001):
		s = utils.isqrt(D)
		if s*s == D:
			continue # Skip perfect squares
		worst = max(worst, (get_min_x_sol(D), D))
	return worst[1], "D for which minimum solution in x is highest (x=%d)" % (worst[0],)
