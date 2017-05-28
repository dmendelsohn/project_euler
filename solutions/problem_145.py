import utils

def compute(verbose=False):
    # Odd-length reversible numbers always have "overflow"
    #   Recurrence in odd case: r(n) = 20*25*r(n-4) for n>=4
    #   Base odd case: r(3) = 100
    #   Notice that r(1)=r(5)=r(9)=0
    # Even-length reversible numbers never have "overflow"
    #   Recurrence in even case: r(n) = 30*r(n-2)
    #   Base even case: r(2) = 20 (or r(0) = 1)
    MAX_DIGITS = 9  # (inclusive)
    results = {} # Maps num digits to num reversible #s of that length
    results[1] = 0
    results[2] = 20
    results[3] = 100
    for n in range(4, MAX_DIGITS+1):
        if n%2==0:
            results[n] = 30*results[n-2]
        else:
            results[n] = 20*25*results[n-4]
    answer = 0
    for n in range(1, MAX_DIGITS+1):
        answer += results[n]
    return answer, 'Number of reversible numbers below 10**{}'.format(MAX_DIGITS)

