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

def prime_factorize(long x): # Returns dict of factors to multiplicity
    cdef int i
    if x == 1:  # Handle this edge case
        return {}
    cdef int[:] primes = array.array('i', (0,)*18) # Max number of prime factors for num < 2^64
    cdef int[:] mults = array.array('i', (0,)*18)
    cdef int length = 0
    i = 2
    while i <= isqrt(x):
        if x%i == 0:
            if length > 0 and primes[length-1] == i:
                mults[length-1] += 1
            else:
                length += 1
                primes[length-1] = i
                mults[length-1] = 1
            x //= i
        else:
            i += 1
    # Leftover x is prime
    if length > 0 and primes[length-1] == x:
      mults[length-1] += 1
    else:
        length += 1
        primes[length-1] = x
        mults[length-1] = 1
    d = {} # Build dictionary for return
    for i in range(length):
        d[primes[i]] = mults[i]
    return d



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

cpdef p34_helper():
    cdef int[:] facts = array.array('i', utils.get_first_factorials(10))
    cdef int i, j
    cdef int total = 0
    cdef int sum_of_facts
    for i in range(10, 7*facts[9]):
        sum_of_facts = 0
        j = i
        while j > 0:
            sum_of_facts += facts[j%10]
            j //= 10
        if i == sum_of_facts:
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
    MAX = 2400
    cdef int[:] pent = array.array('i',(i*(3*i-1)>>1 for i in range(1,MAX)))
    best = 10**9
    for diff in range(1, MAX-1):
        for i in range(1, MAX-1-diff):
            j = i + diff
            ival = pent[i]
            jval = pent[j]
            if (jval - ival) > best:
                break
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

def p70_helper_old(int max_num):
    cdef int[:] phis = utils.get_first_totients(max_num)
    cdef float min_ratio = 1.01 # Empirically found upper bound
    cdef float ratio
    cdef int i, phi, min_index
    for i in range(2,len(phis)):
        phi = phis[i]
        if phi != 0:
            ratio = 1.0*i/phi
            if ratio < min_ratio:
                if p70_is_permutation(i,phi):
                    min_ratio = ratio
                    min_index = i
    print(min_ratio)
    return min_index

# Assumes number is product of two primes
def p70_helper():
    cdef int[:] primes = utils.get_first_primes(10**4)
    cdef int i, j, phi, n
    cdef float ratio
    cdef int best_n = 0
    cdef float best_ratio = 1.001
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            phi = (primes[i]-1) * (primes[j]-1)
            n = primes[i]*primes[j]
            ratio = 1.0*n/phi
            if n < 10**7 and ratio < best_ratio:
                if p70_is_permutation(n, phi):
                    best_ratio = ratio
                    best_n = n
    return best_n