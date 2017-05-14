# Compute number of ways to fill length-50 strip with length-2, 3, or 4 bars (without mixing)
def compute(verbose=False):
    BARS = [2,3,4]
    LENGTH = 50
    def compute_num_ways(strip_length, bar_length):
        memo = [1] # memo[n] is number of solutions for strip of length-n
        for n in range(1, strip_length+1):
            num_sols = memo[-1]
            if n >= bar_length:
                num_sols += memo[-bar_length]
            memo.append(num_sols)
        return memo[strip_length]-1 # Ignore "empty" strip

    answer = sum(compute_num_ways(LENGTH, bar) for bar in BARS)
    text = '# of ways to fill {} unit strip w/ length (2,3,4) bars (w/o mixing)'.format(LENGTH)
    return answer, text