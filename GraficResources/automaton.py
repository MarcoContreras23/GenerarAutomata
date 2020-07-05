from Resources.state import State


class Automaton:

    def __init__(self):
        self.root = None
        self.states = []
        self.visited = []

    def addRoot(self, value, adj, pos):
        if self.root is None:
            self.root = State(value, adj, pos)
            self.states.append(self.root)
        elif self.root is None:
            self.addNode(self.root)

    def addNode(self, node):
        if node not in self.states:
            self.states.append(node)
