from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.disjoint_set = {}

    def node_initializer(self, node):
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
            return False
        else:
            self.disjoint_set[parent_a] = parent_b
            return True

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_mst(self):
        final_weight = 0
        for x,y,z in self.graph:
            self.node_initializer(x)
            self.node_initializer(y)
        for u, v, w in sorted(self.graph, key=lambda item: item[2]):
            if self.union(u, v):
                final_weight += w
        return final_weight


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    print("minimum cost : ",g.find_mst())
