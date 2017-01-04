import utils

# Add all numbers that can't be written as sum of two abundant numbers
def compute():  # Kinda slow
	def get_all_possible_sums(nums): #returns a set, input must be sorted
		d = set()
		for i in range(len(nums)):
			for j in range(i, len(nums)):
				d.add(nums[i]+nums[j])
		return d
	MAX=28123  # Thanks, math!
	abundant_nums = sorted([i for i in range(12, MAX) if i < utils.sum_divisors(i)])
	possible = get_all_possible_sums(abundant_nums)
	total = sum(i for i in range(1, MAX) if i not in possible)
	return total, "Sum of all numbers that cannot be written as sum of two abundant numbers"
