import utils
import fast

# Find lowest n for which the number of bouncy nums up to n is exactly 99% of n
# A bouncy number is a number whose digits have both increases and decreases
def compute(verbose=True):
    NUM_PERCENT = 99
    def is_bouncy(num):
        digits = utils.get_digits(num, reverse=True)
        has_increase = False
        has_decrease = False
        for i in range(len(digits)-1):
            diff = digits[i+1]-digits[i]
            if diff > 0:
                has_increase = True
            if diff < 0:
                has_decrease = True
        return has_increase and has_decrease
    n, count = 0, 0
    while True:
        n += 1
        if fast.p112_is_bouncy(n):
            count += 1
        if count*100 == n*NUM_PERCENT:
            break
    return n, 'Least n for which proportion of bouncy numbers <= n is 99%'
