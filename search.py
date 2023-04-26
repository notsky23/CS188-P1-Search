# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

"""
the tree traversal algorithm
"""
def treeTraversal(problem, frontier):
    # print("DS", frontier.list)
    frontier.push((None, problem.getStartState(), None, 0))
    # print("DS", frontier.list)
    explored = dict()

    'Next path function'
    def path(step):
        state, move = explored[hash(step)]
        # print("STATE", state, "MOVE", move)
        # print("EXPLORED", explored)
        moves = []

        # print("MOVES", moves)
        # print("STATE", state, "ACTION", action)
        while move is not None:
            moves.append(move)
            state, move = explored[hash(state)]
            # print("MOVES", moves)
            # print("STATE", state, "MOVE", move)

        return moves[::-1]

    'add successors to frontier'
    def addSuccessorsToFrontier(start, cost):
        for next, move, additionalCost in problem.getSuccessors(start):
            # print("SUCCESSORS", problem.getSuccessors(start))
            # print("NEXT", next, "MOVE", move, "ADD COST", additionalCost)
            if hash(next) not in explored:
                frontier.push((start, next, move, (cost + additionalCost)))

    'Loop to step on next node then finding and adding successor nodes to list'
    'List could be a stack, queue, or priority queue'
    while not frontier.isEmpty():
        # print("DS", frontier.list)
        current, next, move, cost = frontier.pop()
        # print("CURRENT", current, "NEXT", next, "MOVE", move, "COST", cost)

        if hash(next) in explored:
            continue

        explored[hash(next)] = (current, move)
        # print("EXPLORED", explored)

        'move pacman'
        if problem.isGoalState(next):
            # print("PATH", path(next))
            return path(next)

        addSuccessorsToFrontier(next, cost)
        # print("SUCCESSORS", frontier.list)

    return []


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    'call stack data structure because DFS is LIFO'
    return treeTraversal(problem, util.Stack())


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    'call queue data structure because BFS is FIFO'
    return treeTraversal(problem, util.Queue())

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    def frontierFunction(item):
        stateStart, stateEnd, move, cost = item
        return cost

    return treeTraversal(problem, util.PriorityQueueWithFunction(frontierFunction))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    def frontierFunction(item):
        stateStart, stateEnd, move, cost = item
        return cost + heuristic(stateEnd, problem)

    return treeTraversal(problem, util.PriorityQueueWithFunction(frontierFunction))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
