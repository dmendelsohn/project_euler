import utils

# Compute number of subset-pairs to chck to ensure condition 1 of special sum set
def compute(verbose=False):
    # Observation 1: Only need to compare subsets of the same size, since
    #   different size would guarantee different sum (under condition 2 of special sum set)
    #   we're only responsible for checking condition 1
    # Observation 2: To count how many pairs of subsets (each of size i) we need to check, we need
    #   need to make sure that one subset does not "dominate" another (i.e. for some index j, the order
    #   j element in subset A needs to be greater than B, and vice versa for some other index k).
    # Observation 3: For any 2*i elements in the overall set, the number of ways to partition them
    #   into two subsets, meeting the above criterion, is just the number of INVALID ways of writing
    #   i parentheses (consider left parens as elts in subset A and right parens as elts in subset B).
    #   To avoid double counting, assume first paren is a left paren.
    # Observation 4: Mathematically, the above quantity is 1/2 * (2i choose i) - C_i, where C_i is the
    #   ith Catalan number.  This reduces to the math below since C_i = 1/(i+1) * (2*i choose i).
    def checks_required(n):
        total = 0
        for i in range(2, n//2 + 1):
            total += (utils.nCr(n, 2*i) * utils.nCr(2*i, i) * (i-1) // (2 * (i+1)))
        return total
    return checks_required(12), "Number of subset-pairs to check to ensure condition 1 of special sum set"