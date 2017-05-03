# Find the sum of all the multiples of 3 or 5 below 1000.
def compute(verbose=False):
    answer = sum(n for n in range(1000) if n%3==0 or n%5==0)
    return answer, "The sum of all multiples of 3 or 5 below 1000"
