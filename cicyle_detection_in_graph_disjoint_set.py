class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.disjoint_set = {}

    def addEdge(self, u, v):
        self.graph.append([u,v])

    def node_inittializer(self, node):
        self.disjoint_set[node] = node

    def find(self, node):
        if self.disjoint_set[node] == node:
            return node
        else:
            return self.find(self.disjoint_set[node])

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return True
        else:
            self.disjoint_set[parent_a] = parent_b
            return False

    def detect_cicyle(self):
        for x, y in self.graph:
            self.node_inittializer(x)
            self.node_inittializer(y)
        for x, y in self.graph:
            if self.union(x, y):
                print("cicyle detected in given network!")
                return True
        print("No cicyle found in given network!")
        return False


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(4, 5)
    g.addEdge(3, 2)
    g.detect_cicyle()
