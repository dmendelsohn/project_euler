# Box has red disks and blue disks.  Certain distributions give us a 1/2 chance of drawing
# two blues in a row without replacement.  What is the number of blue balls in the first such
# distribution with over one trillion disks total?
def compute(verbose=False):
    # Observation: letting x=2t-1 and y=2b-1 (t for 'total' and b for 'blue'),
    # we need to solve x^2 - 2y^2 = -1.  I found on the internet that we get all solutions
    # by solvin x_n + y_n * sqrt(2) = (1+sqrt(2))^(2n-1)
    # Muliiply (a + bsqrt(2)) * (1 + sqrt(2)), return (x,y) where result was x+ysqrt(2)
    def multiply(a, b):
        return (a+2*b, a+b)
    a, b = 1, 1
    while a < 2*10**12:
        a, b = multiply(a,b)
        a, b = multiply(a,b)
    return (b+1)//2, 'Number of blue disks (total is %d)' % ((a+1)//2,)
