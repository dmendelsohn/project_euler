import itertools
import utils

def compute(verbose=False):
    APPROX = (20,31,38,39,40,42,45)
    k = 2 # Assume that each elt of solution is within k of approximate solution (it turns out it's within 0)
    best_t = APPROX
    best_sum = sum(best_t)+1
    for delta in itertools.product(range(-k,k+1), repeat=7):
        t = tuple(sum(x) for x in zip(APPROX, delta))
        if sum(t) >= best_sum:
            continue # Not better than what we already have
        is_valid = True
        for i in range(len(t)-1):
            if t[i] >= t[i+1]:
                is_valid = False
                break
        if not is_valid:
            continue # Not ordered, unique tuple

        if sum(t[:2]) <= t[-1] or sum(t[:3]) <= sum(t[:4:-1]) or sum(t[:4]) <= sum(t[:3:-1]):
            continue # Doesn't meet second condition

        # Note: we could speed this up using logic in problem 106; not worth the complexity
        # Make sure no two pairs have same sum (to optimize: only check disjoint pairs)
        pair_sums = set()
        is_valid = True
        for pair in itertools.combinations(t, 2):
            if sum(pair) in pair_sums:
                is_valid = False
                break
            pair_sums.add(sum(pair))
        if not is_valid:
            continue

        # Make sure no two trips have same sum (to optimize: only check disjoint trips)
        trip_sums = set()
        is_valid = True
        for trip in itertools.combinations(t, 3):
            if sum(trip) in trip_sums:
                is_valid = False
                break
            trip_sums.add(sum(trip))
        if not is_valid:
            continue

        best_t = t
        best_sum = sum(best_t)

    answer = utils.concatenate_ints(best_t)
    return answer, "Set-string for optimal special sum set for n=7"
