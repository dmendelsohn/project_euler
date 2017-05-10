import fast

# Find sum of minimal product-sum numbers for 2<=k<=12000
#@profile
def compute(verbose=False):
    ans = fast.p88_helper()
    return ans, 'Sum of minimal product-sum number for 2<=k<=12000'

if __name__ == "__main__":
    print(compute())
