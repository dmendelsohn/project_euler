import numpy as np
import utils

def matrix_power_mod(A, n, m): # Calculate A^n mod m
    digits = utils.get_digits(n, base=2, reverse=True)
    result = np.identity(A.shape[0])
    for bit in digits:
        result = np.dot(result, result)%m
        if bit == 1:
            result = np.dot(result, A)%m
    return result

def compute(verbose=False):
    A = np.zeros((18,18), dtype=np.uint64)
    for i in range(8):
        A[i,i+1] = 1
        A[i+9,i+10] = 1
    A[8,:9] = 1
    A[17,9:] = 10
    for i in range(9):
        A[17,i] = 9-i

    def f_mod(n,m):
        A_power = utils.matrix_power_mod(A, n, m)
        return int(A_power[17,8])  # The bottom-right corner of A_power * initial state

    # I had to split the problem into two parts for due to some overflow issue
    # Answer is still unique given answer mod 2**9 and 5**9 due to Chinese Remainder Theorem
    answer2 = sum(f_mod(13**i, 2**9) for i in range(1, 18))%(2**9)
    answer5 = sum(f_mod(13**i, 5**9) for i in range(1, 18))%(5**9)
    n = answer5
    while n%(2**9) != answer2:
        n += 5**9
    return n, 'Sum of specified f(n)'
