import utils
import fast
import array

# Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
# Warning: This takes a while (25s)
def compute(verbose=False):
    MAX = 10**7
    phis = utils.get_first_totients(MAX)
    arr = array.array('i',phis)
    answer = fast.p70_helper(arr)
    text = "The n for which phi(n) is a permutation of n and n/phi(n) is minimized"
    return answer, text

if __name__ == "__main__":
    print(compute()[0])
