# How many letters to write out 1 through 1000?
def compute(verbose=False):
    def num_letters(n):  # Only works 1...1000
        HUNDRED, AND, ONE_THOUSAND = 7, 3, 11
        ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4] # Number of letters in one, two, ...
        tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6] # Number of letters in -, ten, twenty, ...
        teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # Number of letters in ten, eleven, twelve ...
        if n >= 10 and n < 20:  # Handle 'teens' edge case first
        	return teens[n-10]
        elif n < 100:
        	return tens[n//10] + ones[n%10]
        elif n == 1000:
        	return ONE_THOUSAND
        else:
        	count = ones[n//100] + HUNDRED
        	if n%100 != 0:
        		count += num_letters(n%100) + AND
        	return count
    total = sum(num_letters(i) for i in range(1, 1001))
    return total, "Total number of letters to write out one through one thousand"
