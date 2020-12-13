class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.disjoint_set={}
    def node_initializer(self,node):
        self.disjoint_set[node]=node
    def find(self,node):
        if self.disjoint_set[node]==node:
            return node
        else:
            return self.find(self.disjoint_set[node])
    def union(self,a,b):
        parent_a=self.find(a)
        parent_b=self.find(b)
        if parent_a==parent_b:
            return False
        else:
            self.disjoint_set[parent_a]=parent_b
            return True
    def display_structure(self):
        print("node configration : ")
        for x in range(1,self.vertices+1):
            print(x,self.disjoint_set[x])
if __name__ == "__main__":
    g=Graph(5)
    for i in range(1,6):
        g.node_initializer(i)
    g.union(1,3)
    g.union(5,2)
    g.union(4,5)
    g.union(3,2)
    g.union(4,3)
    g.display_structure()
