import wj3
import search as s
import timeout_decorator
from wj3test_problems import tests

# timeout in seconds
TOO_LONG = 20

# default searchers from aima.search to use
default_searchers = [ #s.breadth_first_tree_search,
                     s.breadth_first_graph_search,
                     s.depth_first_graph_search,
                     #s.iterative_deepening_search,
                     #s.best_first_graph_search,
                     s.astar_search]

#@timeout_decorator.timeout(TOO_LONG)
def apply_search_alg(alg, problem):
    """ Returns None if it takes too long """
    try:
        return alg(problem)
    except timeout_decorator.TimeoutError as error:
        print('***** Timeout error *****', end=' ')
        return None

def wj3solve(capacities, start, goal, searchers=default_searchers):
    problem = wj3.WJ3(capacities, start, goal)
    print(f"Solving {problem}\n")
    reachable = problem.reachable_states()
    potential = (capacities[0]+1) * (capacities[1]+1) * (capacities[2]+1)
    print(f"{len(reachable)} of {potential} reachable states: {reachable}")
    print()
    successful_searchers = []
    for alg in searchers:
        print(f"• {alg.__name__}", end=': ')
        solution = apply_search_alg(alg, problem)
        if solution:
            wj3.print_solution(solution)
            successful_searchers.append(alg)
        print()
    print("\nSUMMARY: successors/goal tests/states generated/solution")
    if successful_searchers:
        s.compare_searchers([problem], [], searchers=successful_searchers)

def solve_all(plist):
    for capacities, start, goal in plist:
        print('**********************************************************************')
        try:
            wj3solve(capacities, start, goal)
        except Exception as e:
            print(f'*** ERROR {e} **')
        print()

def firstN(arg, n):
    arglist = list(arg)[:n]
    arglist.append('...')
    return arglist

solve_all(tests)
