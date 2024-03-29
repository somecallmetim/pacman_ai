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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"
    # this list keeps track of the tiles we've already explored
    exploredTiles = []

    # stores tiles we haven't checked yet
    unexploredTiles = util.Stack()

    # currentTile contains a triple that has it's coordinates and
    # the path that was used to get to it (extremely important!).
    currentTile = (problem.getStartState(), [])

    while True:
        # checks to see if the location of the current tile matches the position of our goal tile
        if problem.isGoalState(currentTile[0]):
            # returns path that got us to the goal tile
            return currentTile[1]
        else:
            # store's current location into our exploredTiles list
            exploredTiles.append(currentTile[0])

            # successors is a list of 'successors' which are triples that contain neighboring node data
            successors = problem.getSuccessors(currentTile[0])


            for successor in successors:
                if successor[0] not in exploredTiles:
                    # pushes tuple onto unexploredTiles stack that records tile's location and path
                    unexploredTiles.push((successor[0], currentTile[1] + [successor[1]]))

            # if you run out of tiles on the map, something somewhere has gone wrong :(
            if unexploredTiles.isEmpty():
                return []
            # get next unexplored tile
            else:
                currentTile = unexploredTiles.pop()

def breadthFirstSearch(problem):
    # this list keeps track of the tiles we've already explored
    exploredTiles = []

    # stores tiles we haven't checked yet
    unexploredTiles = util.Queue()

    # currentTile contains a triple that has it's coordinates and
    # the path that was used to get to it (extremely important!).
    currentTile = (problem.getStartState(), [])

    while True:
        # checks to see if the location of the current tile matches the position of our goal tile
        if problem.isGoalState(currentTile[0]):
            # returns path that got us to the goal tile
            return currentTile[1]
        else:
            # store's current location into our exploredTiles list
            exploredTiles.append(currentTile[0])

            # successors is a list of 'successors' which are triples that contain neighboring node data
            successors = problem.getSuccessors(currentTile[0])


            for successor in successors:
                if successor[0] not in exploredTiles:
                    # pushes tuple onto unexploredTiles stack that records tile's location and path
                    unexploredTiles.push((successor[0], currentTile[1] + [successor[1]]))

            # if you run out of tiles on the map, something somewhere has gone wrong :(
            if unexploredTiles.isEmpty():
                return []
            # get next unexplored tile
            else:
                currentTile = unexploredTiles.pop()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # this list keeps track of the tiles we've already explored
    exploredTiles = []

    # stores tiles we haven't checked yet
    unexploredTiles = util.PriorityQueue()

    # currentTile contains a triple that has it's coordinates and
    # the path that was used to get to it (extremely important!).
    # last argument is the tile's priority queue value
    currentTile = (problem.getStartState(), [], 0)

    while True:
        # checks to see if the location of the current tile matches the position of our goal tile
        if problem.isGoalState(currentTile[0]):
            # returns path that got us to the goal tile
            return currentTile[1]
        else:
            # store's current location into our exploredTiles list
            exploredTiles.append(currentTile[0])

            # successors is a list of 'successors' which are triples that contain neighboring node data
            successors = problem.getSuccessors(currentTile[0])


            for successor in successors:
                if successor[0] not in exploredTiles:
                    # getting the new path and cost here for easier readability
                    newPath = currentTile[1] + [successor[1]]
                    newCost = currentTile[2] + successor[2]
                    # pushes triple onto unexploredTiles stack that records tile's location and path
                    # also passes cost in for the priority queue to use
                    unexploredTiles.push((successor[0], newPath, newCost), newCost)

            # if you run out of tiles on the map, something somewhere has gone wrong :(
            if unexploredTiles.isEmpty():
                return []
            # get next unexplored tile
            else:
                currentTile = unexploredTiles.pop()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
