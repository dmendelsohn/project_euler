# Compute number of ways to fill length-50 strip with length-2, 3, or 4 bars (with mixing)
def compute(verbose=False):
    BARS = [2,3,4]
    LENGTH = 50
    memo = [1] # memo[n] is number of solutions for length-n strip
    for n in range(1, LENGTH+1):
        num_sols = memo[-1] # Add black to end
        for bar in BARS:
            if n >= bar:
                num_sols += memo[-bar]
        memo.append(num_sols)

    answer = memo[LENGTH]
    text = '# of ways to fill {} unit strip w/ length (2,3,4) bars (w/ mixing)'.format(LENGTH)
    return answer, text