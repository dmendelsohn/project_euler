import numpy as np
import numpy.linalg as linalg
import numpy.polynomial.polynomial as poly

# Find sum of FITs for 1 - n + n^2 - n^3 + n^4 - ... n^10
def compute(verbose=False):
    N = 10 # Maximum degree (a.k.a. order
    COEFFS = np.array([(-1)**n for n in range(N,-1,-1)])
    POLYVALS = np.polyval(COEFFS, range(1,N+2))
    def OP(k): # Returns a_0, a_1, a_2,...a_{k-1} of OP(k,n)
        # Create Vandermodne matrix, V
        vec = np.array(range(1,k+1))
        V = np.zeros((k,k))
        for n in range(V.shape[1]): # Raise each column to nth power
            V[:,n] = vec**n

        a = np.dot(linalg.inv(V), POLYVALS[:k])
        for i in range(len(a)):
            a[i] = round(a[i])  # Need to round due to precision issues, all a ought to be integers
        return a

    def FIT(k): # Returns first incorrect term of O(k,n) or 0 if O(k,n) isn't BOP
        a = OP(k)
        test_vals = np.polyval(a[::-1], range(1,N+2))
        for i in range(len(POLYVALS)):
            if (POLYVALS[i] - test_vals[i]) > 0.5: # Loose definition of "==" due to precision issues
                return round(test_vals[i])
        return 0

    total = sum(FIT(i) for i in range(1,N+1))
    text = "Sum of FITs of BOPs of 1 + n - n^2 + n^3 - ... + n^10"
    return int(total), text
