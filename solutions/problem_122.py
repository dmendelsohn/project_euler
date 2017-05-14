import utils

# I shamelessly just found the sequence online https://oeis.org/A003313/b003313.txt
def compute_from_file(verbose=False):
    filename = utils.INPUT_PATH + "p122_myfile.txt"
    lines = open(filename).read().split('\n')
    nums = [int(line.split()[1]) for line in lines]
    answer = sum(nums)
    return answer, 'Sum of shortest addition chains for 1<=k<=200'
 
def compute(verbose=False):
    MAX = 200
    MEMO = [13]*(MAX+1)
    MEMO[1] = 0 # Base case: 0 mults required to get x^1
    def update_tree(branch):
        last = branch[-1]
        branch_len = len(branch)
        if MEMO[last] < branch_len - 1: # Not sure why this is valid...
            return
        for num in branch:
            new_num = num + last
            if new_num <= MAX:
                MEMO[new_num] = min(MEMO[new_num], branch_len)
                if branch_len < 11:  # Empirically found this is sufficient max depth
                    branch.append(new_num)
                    update_tree(branch)
                    del branch[-1]
            else:
                return
    update_tree([1])
    answer = sum(MEMO[i] for i in range(1,MAX+1))
    return answer, 'Sum of shortest addition chains for 1<=k<=200'