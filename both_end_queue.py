class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Queue:
    def __init__(self):
        self.head, self.tail = None, None

    def push_node_from_head(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def pop_node_from_head(self):
        if self.head:
            tmp = self.head
            self.head = self.head.next
            return tmp.value
        else:
            return False

    def display(self):
        tmp = self.head
        while tmp != None:
            print(tmp.value, end=" ")
            tmp = tmp.next


if __name__ == "__main__":
    Q = Queue()
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        Q.push_node_from_head(i)
    Q.display()
    while True:
        x = Q.pop_node_from_head()
        if x: print(x, end=" ")
        else: break
