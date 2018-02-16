class Node:
    """
    AIMA: A node in a search tree. Contains a pointer to the parent (the node that this is a successor of)
    and to the actual state for this node. Note that if a state is arrived at by two paths,
    then there are two nodes with the same state.  Also includes the action that got us to this state,
    and the total path_cost (also known as g) to reach the node.  Other functions may add an f and h value;
    see best_first_graph_search and astar_search for an explanation of how the f and h values are handled.
    You will not need to subclass this class.
    """

    def __init__(self, state, parent=None, action=None, path_cost=0):
        "Create a search tree Node, derived from a parent by an action."
        self.state = state
        self.parent = parent
        self.action = action
        if parent:
            self.path_cost = parent.path_cost + path_cost
            self.depth = parent.depth + 1
        else:
            self.path_cost = path_cost
            self.depth = 0

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def nodePath(self):
        "Create a list of nodes from the root to this node."
        x, result = self, [self]
        while x.parent:
            result.append(x.parent)
            x = x.parent
        result.reverse()
        return result

    def expand(self, problem):
        """
        Return a list of nodes reachable from this node.
        """
        return [Node(next, self, act, cost)
        for (next, act, cost) in problem.getSuccessors(self.state)]