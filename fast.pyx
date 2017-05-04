import numpy as np
import array
import math
import utils
import itertools

cdef long isqrt(long n):  # Newton's method
    cdef long x, y
    x = n
    y = (x + 1) >> 1
    while y < x:
        x = y
        y = (x + n // x) >> 1
    return x

cdef long test_pent(long x): # Returns 1 iff sqrt(24x+1)%5 == 6, 0 else
    cdef long y = 24*x+1
    cdef long sqrt = isqrt(y)
    if sqrt**2==y and sqrt%6==5:
        return 1
    else:
        return 0

def test_test_pent(n):
    return test_pent(n)

def permutations(n):
    f = 1
    p = np.empty((2*n-1, math.factorial(n)), np.int64)
    for i in range(n):
        p[i, :f] = i
        p[i+1:2*i+1, :f] = p[:i, :f]  # constitution de blocs
        for j in range(i):
            p[:i+1, f*(j+1):f*(j+2)] = p[j+1:j+i+2, :f]  # copie de blocs
        f = f*(i+1)
    return p[:n, :]

# Will only work up to 64-bit long
def p43_sum_with_property(long[:] perms):
    cdef int i
    cdef long total = 0
    for i in range(len(perms)):
        if p43_has_property(perms[i]):
            total += perms[i]
    return total


p43_mods = array.array('i', (2, 3, 5, 7, 11, 13, 17))
def p43_has_property(long x):
    cdef int i
    for i in (1,3,4,5,6): # Already did check for 2 and 5 in pre-processing
        if ((x//10**(6-i))%1000)%p43_mods[i] != 0:
            return False
    return True

def p44_helper():
    cdef int i, j, ival, jval, best, diff
    cdef int[:] pent = array.array('i',(i*(3*i-1)>>1 for i in range(1,10**4)))
    best = 10**9
    #for i in range(10**4-1):
    #    for j in range(i+1, 10**4-1):
    for diff in range(1, 10**4-1):
        for i in range(1, 10**4-1-diff):
            j = i + diff
            ival = pent[i]
            jval = pent[j]
            if (jval - ival) > best:
                continue
            if test_pent(jval-ival) and test_pent(jval+ival):
                best = jval - ival
    return best, 'Smallest pentagonal difference between two pentagonal numbers whose sum is also pentagonal'

cdef int p70_is_permutation(int x, int y): # In current form, only works up to 2^31
    if (x-y)%9 != 0: # Can't be permutations if different mod 9
        return 0
    cdef int[:] x_freqs = array.array('i', (0,)*10)
    cdef int[:] y_freqs = array.array('i', (0,)*10)
    while x > 0:
        x_freqs[x%10] += 1
        x //= 10
    while y > 0:
        y_freqs[y%10] += 1
        y //= 10
    cdef int i
    for i in range(10):
        if x_freqs[i] != y_freqs[i]:
            return 0
    return 1

def p70_helper(int[:] phis):
    cdef float min_ratio = 100
    cdef float ratio
    cdef int i, phi, min_index
    for i in range(2,len(phis)):
        phi = phis[i]
        if phi != 0 and p70_is_permutation(i, phi):
            ratio = 1.0*i/phi
            if ratio < min_ratio:
                min_ratio = ratio
                min_index = i
    return min_index