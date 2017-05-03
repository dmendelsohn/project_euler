import utils

# What is index of first Fibonacci number to contain 1000 digits?
def compute(verbose=False):
	a, b, count = 1, 1, 2
	while (utils.num_digits(b) < 1000):
		a, b, count = b, a + b, count + 1
	return count, "The index of the first Fibonacci number with 1000 digits"
