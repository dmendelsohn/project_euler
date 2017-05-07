import utils
import fast
import array

# Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
def compute(verbose=False):
    MAX = 10**7
    answer = fast.p70_helper()
    text = "The n for which phi(n) is a permutation of n and n/phi(n) is minimized"
    return answer, text

if __name__ == "__main__":
    print(compute()[0])
