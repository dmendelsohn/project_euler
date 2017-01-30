import utils

# Find the last ten digits of 28433 * (2^7830457) + 1
def compute():
	answer = (28433 * utils.power_mod(2, 7830457, 10**10) + 1)%(10**10)  # Ignore the +1 for now
	return answer, 'Last ten digits of 28433 * (2^7830457) + 1'
