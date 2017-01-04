import utils

# Get the highest proper fraction with d <= 10^6 that's strictly less than 3/7
def compute():
	REF = (3,7)
	MAX_DEN = 10**6
	max_so_far = (0,1)  # maximum fraction strictly less than REF, in (num, den) form
	for d in range(2,MAX_DEN+1):
		n = int(1.0*d*REF[0]/REF[1])
		if (d*REF[0])%REF[1] == 0:
			n -= 1  # need to be strictly less than REF
		f = utils.simplify_frac(n, d)
		if utils.frac_gt(f, max_so_far):
			max_so_far = f
	return max_so_far[0], "Fraction immediately preceding %d/%d is %d/%d" % (REF[0], REF[1], max_so_far[0],max_so_far[1])
