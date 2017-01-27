# The sum of even Fibonacci numbers below 4 million
def compute():
	values = [1,2]
	while (values[-1] < 4*10**6):
		values.append(values[-1] + values[-2])
	return sum(v for v in values if v%2==0), "Sum of all even Fibonacci numbers below 4 million"
