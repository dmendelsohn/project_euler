import numpy as np
import array
import utils
import math
from libcpp.set cimport set as cset
from libcpp.vector cimport vector
from libcpp.pair cimport pair

## cdef only helpers for helpers

cdef long isqrt(long n):  # Newton's method
    cdef long x, y
    x = n
    y = (x + 1) >> 1
    while y < x:
        x = y
        y = (x + n // x) >> 1
    return x

cdef long gcd(long a, long b):
    while b:
        a, b = b, a%b
    return a

cdef long sum_of_func_of_digits(long x, int[:] mapping):
    cdef int total = 0
    while x > 0:
        total += mapping[x%10]
        x //= 10
    return total

cdef int num_digits(int x):
    return 1+int(math.log10(x))

cdef int is_prime(int x):
    cdef int i, max_num
    if x <= 1:
        return 0
    elif x <= 3:
        return 1
    elif x%2 == 0:
        return 0
    else:
        i = 3
        max_num = isqrt(x)
        while i <= max_num:
            if x%i==0:
                return 0
            i += 2
        return 1


## Individual problem helpers

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
        sum_of_facts = sum_of_func_of_digits(i, facts)
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

cdef long p44_test_pent(long x): # Returns 1 iff sqrt(24x+1)%5 == 6, 0 else
    cdef long y = 24*x+1
    cdef long sqrt = isqrt(y)
    if sqrt**2==y and sqrt%6==5:
        return 1
    else:
        return 0

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
            if p44_test_pent(jval-ival) and p44_test_pent(jval+ival):
                best = jval - ival
    return best, 'Smallest pentagonal difference between two pentagonal numbers whose sum is also pentagonal'

cpdef int p60_is_edge(int x, int y):
    cdef int a = x*(10**(num_digits(y)))+y
    cdef int b = y*(10**(num_digits(x)))+x
    return is_prime(a) and is_prime(b)

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

def p73_helper():
    cdef int n = 12000 # Max denominator (Farey sequence n=12000)
    cdef int a = 1
    cdef int b = 3 # Fraction 1/3
    cdef int c = 4000
    cdef int d = 11999 # Next biggest one after 1/3, found by trial and error
    cdef int count = 0
    cdef int e, f
    while d != 2: # While we haven't reached 1/2
        e, f = (n + b)//d*c - a, (n + b)//d*d - b
        a, b, c, d = c, d, e, f # Shift
        count += 1
    return count

def p74_helper():
    cdef int memo_len = int(2.5*10**6) # Found by trial and error
    cdef int[:] memo = array.array('i', (0,)*memo_len)
    cdef int[:] facts = array.array('i', utils.get_first_factorials(10))
    # Set manual values
    memo[1] = 1
    memo[2] = 1
    memo[145] = 1
    memo[40585] = 1
    memo[871] = 2
    memo[45361] = 2
    memo[872] = 2
    memo[45362] = 2
    memo[169] = 3
    memo[363601] = 3
    memo[1454] = 3
    cdef int count = 0
    cdef int i, j, base_num
    cdef int[:] chain = array.array('i', (0,)*100) # Reusable buffer
    cdef int chain_len = 0
    for i in range(1, 10**6):
        if memo[i] == 0:
            j = i
            chain_len = 0
            while memo[j] == 0:
                chain[chain_len] = j
                chain_len += 1
                j = sum_of_func_of_digits(j, facts)
            base_num = memo[j]
            for j in range(chain_len):
                memo[chain[j]] = base_num + chain_len - j
        if memo[i] == 60:
            count += 1
    return count

# How many L < 1.5 million are sum of EXACTLY ONE Pythagorean triple
def p75_helper():
    MAX_NUM = 1500000
    cdef int[:] MEMO = array.array('i', (0,)*MAX_NUM)
    cdef int m, n, base_perim, L
    for m in range(1, isqrt(MAX_NUM)):
        for n in range(1, m):
            if gcd(m,n) != 1 or (m*n)%2==1:
                continue # Not a primitive triple
            base_perim = 2*m*(m+n)
            L = base_perim
            while L < MAX_NUM:  # Account for multiples of primitive triples with L small enough
                MEMO[L] += 1
                L += base_perim
    cdef int i
    cdef count = 0
    for i in range(MAX_NUM):
        if MEMO[i] == 1:
            count += 1
    return count


def p78_helper():
    cdef int[:] MEMO =  array.array('i', (-1,)*60000) # Only need this many, by trial and error
    MEMO[0] = 1 # By definition, p(0)=1
    cdef int n = 1
    cdef int count, k, pent
    while True:
        count = 0
        k = 1
        pent = k*(3*k-1)>>1
        while pent <= n:
            if k%2==1:
                count += MEMO[n-pent]
            else:
                count -= MEMO[n-pent]
            k = -k
            if k > 0:
                k += 1
            pent = k*(3*k-1)>>1
        MEMO[n] = count%(10**6)
        if MEMO[n] == 0:
            return n
        n += 1

def p87_helper():
    cdef int MAX = 5*10**7
    cdef int[:] PRIMES = array.array('i', utils.get_first_primes(isqrt(MAX)+2000))
    cdef int quad_max = int(MAX**0.25)
    cdef int trip_max = int(MAX**(1.0/3))
    cdef int dub_max = int(MAX**0.5)
    cdef cset[int] results
    cdef int i, j, k, s
    i = 0
    while PRIMES[i] <= quad_max:
        j = 0
        trip_max = int((MAX-PRIMES[i]**4)**(1.0/3))
        while PRIMES[j] <= trip_max:
            k = 0
            dub_max = int((MAX-PRIMES[i]**2-PRIMES[j]**3)**0.5)
            while PRIMES[k] <= dub_max:
                s = PRIMES[i]**4 + PRIMES[j]**3 + PRIMES[k]**2
                if s < MAX:
                    results.insert(s)
                k += 1
            j += 1
        i += 1
    return results.size()

cdef struct p88_summary:
    int length
    int sum
    int prod

# Returns list of multiset summaries for multisets meeting constraints
cdef vector[p88_summary] p88_get_multisets(int max_sum, int max_prod, int max_elt):
    cdef vector[p88_summary] results, subresults
    cdef p88_summary s = p88_summary(length=0, sum=0, prod=1)
    results.push_back(s)
    cdef int highest_possible = min(max_elt, max_prod, max_elt)
    cdef int i, j
    for i in range(2, 1+highest_possible):
        subresults = p88_get_multisets(max_sum-i, int(max_prod/i), i)
        for j in range(len(subresults)):
            subresults[j].length += 1
            subresults[j].sum += i
            subresults[j].prod *= i
        results.insert(results.end(), subresults.begin(), subresults.end())
    return results


def p88_helper():
    cdef int K = 12000
    cdef int k, prod
    cdef int[:] sols = array.array('i', [2*k for k in range(K+1)])
    cdef int max_size = int(math.log(2*K, 2))
    cdef vector[p88_summary] multisets = p88_get_multisets(K+max_size, 2*K, K)
    cdef p88_summary m
    for m in multisets:
        prod = m.prod
        k = m.length + prod - m.sum
        if k <= K and prod < sols[k]:
            sols[k] = prod
    cdef int answer = sum(set(sols[2:]))
    return answer

def p95_helper():
    cdef int MAX = 1+10**6
    cdef int[:] sigmas = utils.get_first_sigmas(MAX, proper=True)
    cdef unsigned char[:] seen = array.array('B', (0,)*MAX)
    cdef int[:] chain = array.array('i', (0,)*100) # Assume chains are shorter than 100
    cdef int chain_len = 0
    cdef int i, j, k, loop_start
    cdef int longest_loop_len = 0
    cdef int answer = MAX
    for i in range(1, MAX): # i is start of chain
        j = i
        chain_len = 0
        while j < MAX and not seen[j]:
            seen[j] = 1
            chain[chain_len] = j
            chain_len += 1
            j = sigmas[j]

        # Check for index of j in chain, j is start of loop
        k = 0
        loop_start = -1
        while k < chain_len:
            if chain[k] == j:
                loop_start = k
                break
            k += 1
        if loop_start >= 0: # checks that we looped
            if (chain_len - loop_start) > longest_loop_len:
                longest_loop_len = chain_len - loop_start
                answer = chain[loop_start]
                for k in range(loop_start, chain_len):
                    answer = min(answer, chain[k])
    return answer        
    #return min(longest_chain), 'Minimum element in longest "sum of proper divisors" chain'

cdef int p104_is_pandigital(int num):
    cdef int agg = 0
    while num > 0:
        agg += (1<<(num%10))
        num //= 10
    return agg == (2**10-2)

def p104_helper():
    cdef int prev_fib = 1
    cdef int fib = 1
    cdef double phi = 0.5*(1+5**0.5)
    cdef double phi_power = phi**2 / (5**0.5)
    cdef int n = 2
    while True:
        if p104_is_pandigital(fib) and p104_is_pandigital(int(phi_power)):
        #if p104_is_pandigital(fib):
        #if p104_is_pandigital(int(phi_power)):
            break
        prev_fib, fib = fib, (prev_fib+fib)%(10**9)
        phi_power *= phi
        if phi_power >= 10**9:
            phi_power /= 10
        n += 1
    return n

def p112_is_bouncy(unsigned int num):
    cdef int num_increases = 0
    cdef int num_decreases = 0
    cdef int digit, prev_digit
    prev_digit = num%10
    num //= 10
    while num > 0:
        digit = num%10
        if digit > prev_digit:
            num_increases += 1
        elif digit < prev_digit:
            num_decreases += 1
        prev_digit = digit
        num //= 10
    return (num_increases > 0) and (num_decreases > 0)

def p126_helper(int limit=20000, int target=1000):
  cdef int i,j,k,l,S,E,size
  cdef int MAX_DIM = limit//4
  cdef int[:] C = array.array('i',[0]*limit)
  for i in range(1, MAX_DIM):
    for j in range(i, MAX_DIM):
      if (6*i*j >= limit):
        break # Surface area already exceeds limit
      for k in range(j, MAX_DIM):
        S = 2*(i*j + i*k + j*k)
        E = 4*(i+j+k)
        size = S # First layer size
        l = 1  # Layer counter
        while size < limit:
          C[size] += 1
          l += 1
          size += (E + 8*(l-2))

  cdef int n
  for n in range(1, limit):
    if C[n] == target:
      return n, 'Lowest number that is size of a layer of {} cuboids'.format(target)
  return -1, 'No solution found below {}'.format(limit)

def p127_get_total(ab, r, int MAX=120000):
  cdef long[:] possible_ab = array.array('l', ab)
  cdef long[:] rad = array.array('l', r)
  cdef int ai, bi, a, b, c
  cdef long rad_abc
  cdef int total = 0
  for ai in range(len(possible_ab)):
    for bi in range(ai+1, len(possible_ab)):
      a = possible_ab[ai]  # We aren't doing a<b, but (a,b) are unique
      b = possible_ab[bi]
      rad_abc = rad[a]*rad[b]
      if rad_abc >= MAX//2:
        break
      c = a+b
      if c < MAX:
        rad_abc *= rad[c]
        if rad_abc < c and gcd(a,b) == 1:
          total += c
  return total

