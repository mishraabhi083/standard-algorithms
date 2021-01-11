class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.connections = []


def traverse_graph_DFS(node):
    # print(node.value)
    if node.connections == [] or node.visited == True:
        return
    else:
        node.visited = True
        for i in node.connections:
            print(f"{node.value} --> {i.value}")
            traverse_graph_DFS(i)
def traverse_graph_BFS(node):
    queue=[node]
    while queue!=[]:
        current_node=queue.pop(0)
        if not current_node.visited:
            current_node.visited=True
            for i in current_node.connections:
                queue.append(i)
                print(f"{current_node.value} --> {i.value}")



if __name__ == "__main__":
    graph = []
    edge_list = [
        (1, 2, 5),
        (2, 4, 8),
        (2, 5, 15),
        (3, 1, 25),
        (4, 3, 10),
        (4, 5, 20),
    ]
    number_of_vertices = 5
    for i in range(number_of_vertices):
        graph.append(Node(i + 1))
    for x, y, z in edge_list:
        graph[x - 1].connections.append(graph[y - 1])

    traverse_graph_BFS(graph[0])
