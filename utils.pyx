#from cython cimport array
import array
import math
import operator
import collections
import itertools
from functools import reduce


INPUT_PATH = 'inputs/'

def num_digits(x):
    return 1+int(math.log10(x))

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def nCr(n, r):
    return reduce(operator.mul, range(n-r+1, n+1)) // reduce(operator.mul, range(1,r+1))

def power_mod(a, b, m): # Find a^b mod m
    if b == 0: # Base case
        return 1
    if b%2 == 0:
        x = 1
    else:
        x = a # Handle extra factor of a
    return (x*(power_mod(a, b//2, m)**2))%m


def factorial(n):
    f = 1
    while n > 1:
        f, n = f*n, n-1
    return f

def get_first_factorials(max_num):
    fact = [1]
    for i in range(1, max_num):
        fact.append(i*fact[i-1])
    return fact

def simplify_frac(a, b=None):
    if b: # They gave numerator and denom separately
        g = gcd(a, b)
        return a//g, b//g
    return simplify_frac(a[0], a[1]) # They gave it as a tuple

def frac_lt(a, b):  # a and b are both (num,den) fractions
    return a[0]*b[1] < a[1]*b[0]

def frac_eq(a, b):  # a and b are both (num, den) fractions
    return a[0]*b[1] == a[1]*b[0]

def frac_gt(a, b):  # a and b are both (num, den) fractions
    return a[0]*b[1] > a[1]*b[0]

def frac_le(a, b):  # a and b are both (num, den) fractions
    return a[0]*b[1] <= a[1]*b[0]

def frac_ge(a, b):  # a and b are both (num, den) fractions
    return a[0]*b[1] >= a[1]*b[0]

def isqrt(n):  # Newton's method
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def is_square(n):
    return isqrt(n)**2 == n

def make_number(digits, int base=10, reverse=False): # Assume digits are in low->high order
    cdef int a, b
    if reverse:
        d = digits[:]
    else:
        d = digits[::-1]
    return reduce(lambda a,b: a*base+b, d, 0)

def get_digits(x, int base=10, reverse=False): # Returns list of digits, starting with low order, in decimal
    if x == 0:
        return [0]
    digits = []
    while x > 0:
        digits.append(x%base)
        x //= base
    if reverse:
        digits.reverse()
    return tuple(digits)

def get_sorted_digits(x):
    return tuple(sorted(get_digits(x)))

cdef int[:] get_digit_freqs(int n):
    cdef int freqs[10]
    freqs = [0,0,0,0,0,0,0,0,0,0]
    while n > 0:
        freqs[n%10] += 1
        n //= 10
    return freqs

def is_permutation(int x, int y): # In current form, only works up to 2^31
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
            return False
    return True

def sum_of_digits(x, int base=10):  # This way I won't have to make a list every time
    cdef int total
    if x == 0:
        return 0
    total = 0
    while x > 0:
        total += x%base
        x //= base
    return total

def is_palindrome(x, base=10):
    digits = get_digits(x, base=base)
    return digits == digits[::-1]

def prime_factorize(x): # Returns dict of factors to multiplicity
    cdef int i
    if x == 1:  # Handle this edge case
        return {}
    d = {}
    i = 2
    while i <= isqrt(x):
        if x%i == 0:
            d[i] = d.get(i,0)+1
            x //= i
        else:
            i += 1
    d[x] = d.get(x,0)+1 # Leftover x is prime
    return d

def multiply_factorizations(a, b):
    cdef int p
    primes = set(a.keys()).union(set(b.keys()))
    return {p: a.get(p, 0) + b.get(p, 0) for p in primes}

def count_divisors(d):  # d is factorization dictionary
    cdef int a,b
    return reduce(lambda a,b: a*(b+1), d.values(), 1)

def num_divisors(x):
    return count_divisors(prime_factorize(x))

def sum_divisors(int n): # Aka sigma(n)
    cdef int total, sqrt, i
    total = 0
    sqrt = isqrt(n)
    for i in range(1, sqrt+1):
        if n%i==0:
            total += i + n//i
    if sqrt**2 == n:
        total -= sqrt #handle perfect square case
    return total

def get_first_sigmas(int n): # Returns [sigma(n) for i in range(n)], using sieve for efficiency
    cdef int i, mul, prod
    sigmas = [0 for i in range(n)]
    for i in range(1, 1+isqrt(n-1)):
        mul = i
        prod = i*mul
        while prod < n:
            sigmas[prod] += (i+mul)
            mul += 1
            prod += i
    for i in range(1, 1+isqrt(n-1)):
        sigmas[i**2] -= i
    return sigmas

def is_prime(int x):
    cdef int i, max_num
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x%2 == 0:
        return False
    else:
        i = 3
        max_num = isqrt(x)
        while i <= max_num:
            if x%i==0:
                return False
            i += 2
        return True

def get_first_primes(int max_num, as_set=False):
    cdef unsigned char[:] sieve = array.array('B', (1,)*(max_num//2))
    cdef int i, num
    for i in range(3, 1+isqrt(max_num),2):
        num = i**2
        if sieve[i>>1]:
            while (num < max_num):
                sieve[num>>1] = 0
                num += 2*i
    if as_set:
        result = {2*i+1 for i in range(1, max_num//2) if sieve[i]}
        result.add(2)
        return result
    else:
        return [2] + [2*i+1 for i in range(1, max_num//2) if sieve[i]]

def get_first_totients(int max_num):  # returns list, including zero element (let's define phi(0)=0)
    primes = get_first_primes(max_num, as_set=False) # Sorted list of relevant primes
    cdef int p, i
    cdef int[:] nums = array.array('i', (1,)*max_num)
    cdef int[:] dens = array.array('i', (1,)*max_num)
    for p in primes:
        for i in range(p, max_num, p):  # All multiples of p
            nums[i] *= (p-1)
            dens[i] *= p
    return [0] + [i//dens[i]*nums[i] for i in range(1, max_num)]

def get_first_num_divisors(int max_num): # returns list, including zero element, (let's say 0 and 1 have 1 divisor)
    cdef int i, num
    sieve = [2 if i > 1 else 1 for i in range(max_num)]  # Already count 1 themselves and 1
    for i in range(2, 1+max_num/2):
        num = 2*i # i is already counted
        while (num < max_num):
            sieve[num] += 1 # Found another divisor
            num += i
    return sieve

def get_permutation(items, index):
    unused = sorted(list(items))
    factorial = get_first_factorials(len(unused))
    result = []
    while unused:
        n = len(unused)-1
        next_item = unused.pop(index // factorial[n])
        result.append(next_item)
        index %= factorial[n]
    return result

def get_num_permutations(l):
    num = math.factorial(len(l))
    mults = collections.Counter(l).values()
    den = reduce(operator.mul, (math.factorial(v) for v in mults), 1)
    return num // den

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return set(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1)))

def get_vocab(): # Will work for most unix systems
    words = open('/usr/share/dict/words', 'rt').read().split()
    return {w: None for w in words}

def load_grid(filename, delim):
    return [list(map(int, row.strip().split(delim))) for row in open(filename).read().strip().split('\n')]

# Often the format required for submissions
def concatenate_ints(iterable):
    return int(''.join(map(str, sorted(iterable))))

