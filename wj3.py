""" A variation on the class water jugs problem. You are given a set
of three jugs with capacities C1, C2 and C3 initially filled with
water in amounts W1, W2 and W3.  Can you end up with exactly G1 thru
Gn liters in the jugs J1 thru Jn?

You're allowed the following six actions: dump the contents of
any jug onto the floor, pour the contents of one jug into
another until either the jug from which you are pouring is empty or
the one you are filling is full, and filling any jug that is not
yet full from a faucet until the it is full.

The cost of each action is 1 plus the amount of water it uses (if any)
from the faucet.  For example, the action of emptying jug 1 costs 1,
and toping off jug 1 if it has capacity five liters but only two
liters of water costs 4.  """

import search as s               # from AIMA code

class WJ3(s.Problem):
    """
    STATE: tuple like (3,2,1) if the three with 3, 2, and 1 liters of water.
    GOAL: a state except with -1 representing a 'don't care', so
      valid goals for this might include (1,1,1) and (-1,2,2).
    PROBLEM: Specify capacities of each jug, initial state and goal """

    def __init__(self, capacities=(12,8,5), initial=(12,0,0), goal=(6,6,0)):
        pass

    def __repr__(self):
        """ Returns a string representing the object """
        pass

    def goal_test(self, state):
        """ Returns True iff state is a goal state """
        pass

    def h(self, node):
        """ Estimate of cost of shortest path from node to a goal """
        pass
    
    def actions(self, state):
        """ generates legal actions for state """
        pass

    def result(self, state, action):
        """ Returns the successor of state after doing action """
        #print(f"Calling result({state},{action}")
        pass
    
    def reachable_states(self):
        """Returns a list of the states that can be reached from the initial state"""
        pass
        
    def path_cost(self, c, state1, action, state2):
        """ Cost of path from start node to state1 assuming cost c to
        get to state1 and doing action to get to state2 """
        pass

def print_solution(solution):
    """If a path to a goal was found, prints the cost and the sequence of actions
    and states on a path from the initial state to the goal found"""
    if not solution:
        print("No solution found 🙁")
    else:
        print("Path of cost", solution.path_cost, end=': ')
        for node in solution.path():
              if not node.action:  # None implies it's the initial state
                  print(node.state, end=' ')
              else:
                  print(f'-{node.action}->{node.state}', end=' ')

