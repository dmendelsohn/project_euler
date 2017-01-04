import utils

# Compute sum of amicable numbers under 10000
def compute():
	arr = [0,1] + [utils.sum_divisors(i) for i in range(2, 10**4)]  #d(0) = 0, d(1) = 1, this won't matter
	amic = 0
	for i in range(len(arr)):
		j = arr[i]
		if j > i and j < len(arr) and i == arr[j]:
			amic += i + j
	return amic, "Sum of amicable numbers under 10000"
