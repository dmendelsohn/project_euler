import utils
from scipy.sparse.csgraph import minimum_spanning_tree as mst
from scipy.sparse import csr_matrix
def compute(verbose=False):
    filename = utils.INPUT_PATH + "/p107_network.txt"
    text = open(filename).read().strip()
    text = text.replace('-','0')
    rows = text.split('\n')
    grid =  [list(map(int, row.strip().split(","))) for row in rows]
    tree = mst(grid)
    original = sum(map(sum, grid))//2
    savings = original - int(csr_matrix.sum(tree))
    return savings, 'Difference between total edge weights and edge weights of MST'
