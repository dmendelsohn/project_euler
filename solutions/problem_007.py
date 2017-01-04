import utils

# What is 10001st prime number
def compute():
	prime_count = 1  # To account for 2, which we skip
	current_number = 1
	while (prime_count < 10001):
		current_number += 2
		if utils.is_prime(current_number):
			prime_count += 1
	return current_number, "The 10001st prime number"
