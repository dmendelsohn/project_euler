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

cdef int p14_collatz(long n, int[:] cache):
    cdef int result
    if n < 10**6 and cache[n] > 0:
            result = cache[n] #Cached
    elif n==1:
        result = 1 # Base case
    elif n%2==0:
        result = 1+p14_collatz(n>>1, cache)
    else:
        result = 1+p14_collatz(3*n+1, cache)
    if n < 10**6:
        cache[n] = result
    return result

def p14_helper(int max_num):
    cdef int[:] cache = array.array('i', (0,)*(max_num))
    cdef int best_length = 0
    cdef int best_i = 0
    cdef int i, length
    for i in range(1,max_num):
        length = p14_collatz(i, cache)
        if length > best_length:
            best_length = length
            best_i = i
    return best_i , "The number under one million that produces longest Collatz chain (%d)" % (best_length,)

cpdef p23_get_possible_sums(abundant_nums, int max_num):
    cdef int[:] nums = array.array('i', abundant_nums)
    cdef int[:] possible = array.array('i', (0,)*max_num)
    cdef int i,j, total
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            total = nums[i] + nums[j]
            if total < max_num:
                possible[total] = 1
    return set([i for i in range(max_num) if possible[i] > 0])

cpdef p30_helper():
    cdef int limit = 2*(10**5)
    cdef int total = 0
    cdef int i, j, sum_of_powers
    for i in range(10,limit):
        sum_of_powers = 0
        j = i
        while j > 0:
            sum_of_powers += (j%10)**5
            j //= 10
        if i == sum_of_powers:
            total += i
    return total

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