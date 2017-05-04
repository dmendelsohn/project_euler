# Modified from Peter Norvig's 2016 Advent of Code solution
# I adde cost_func for edges, the existing function assumed edges all have weight 1
from heapq import heappop, heappush

def astar(start, goal, cost_func, move_func, h_func=None):
    "Find a minimum cost path from start to a goal state"
    if not h_func:
        h_func = lambda s: 0  # Admissible, albeit not very useful, heuristic
    frontier  = [(h_func(start), start)] # A priority queue, ordered by path length, f = g + h
    previous  = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}     # The cost of the best path to a state.
    while frontier:
        (f, s) = heappop(frontier)
        if s == goal:
            return get_path(previous, s)
        for s2 in move_func(s):
            new_cost = path_cost[s] + cost_func(s, s2)
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))

def get_path(previous, s): 
    "Return a list of states that lead to state s, according to the previous dict."
    return ([] if (s is None) else get_path(previous, previous[s]) + [s])

def cost_of_path(path, cost_func):
    if isinstance(path, dict): # There was a failure
        return -1
    elif len(path) < 2:
        return 0
    else:
        return sum(cost_func(path[i],path[i+1]) for i in range(len(path)-1))
