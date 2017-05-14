# Find sum for a in [3,1000] of r_max(a)
# r_max(a) is maximum possible value of (a+1)^n + (a-1)^n mod a^2
def compute(verbose=False):
    # Observation 1: (a+1)^n is always an+1 mod a^2
    # Observation 2: (a-1)^n is an-1 mod a^2 for odd n, -an+1 mod a^2 for even n
    # Observation 3: (1) and (2) mean that r is 2 for even n, 2n for odd n
    # So r_max is a*b, where b is highest even number less than a
    def r_max(a):  # Assumes a >= 3
        if a%2==0:
            return a*(a-2)
        else:
            return a*(a-1)
    
    answer = sum(r_max(a) for a in range(3,1001))
    return answer, 'Sum over 3 <= a <= 1000 of r_max(a)'