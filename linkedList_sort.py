class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addnode(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp:

                if not temp.next:
                    temp.next = Node(data)
                    return temp
                temp = temp.next

    def appendList(self, listHead):
        temp = self.head
        while temp:
            if not temp.next:
                temp.next = listHead
                return self.head
            temp = temp.next

    def display(self, node):
        if node:
            print(node.data, end="->")
            self.display(node.next)

    def length(self):
        counter = 0
        temp = self.head
        while temp:
            counter += 1
            temp = temp.next
        return counter


class MergerSort:
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        res = LinkedList()
        self.tracer_1 = l1
        self.tracer_2 = l2
        while self.tracer_1 and self.tracer_2:
            if self.tracer_1.data < self.tracer_2.data:
                res.addnode(self.tracer_1.data)
            else:
                res.addnode(self.tracer_2.data)
        if self.tracer_1:
            res.appendList(self.tracer_1)
        if self.tracer_2:
            res.appendList(self.tracer_2)

    def sort(self, Llist):
        if Llist:
            Llist.display(Llist.head)
            fast, slow = Llist.head, Llist.head
            while fast:
                fast = fast.next.next if fast.next else None
                slow = slow.next
            l2 = LinkedList().appendList(slow.next)
            l1 = LinkedList().appendList(Llist.head)
            slow.next = None
            return self.merge(self.sort(l1), self.sort(l2))


if __name__ == "__main__":
    dataset = list(map(int, input("Enter nodes : ").strip().split()))
    l = LinkedList()
    for i in dataset:
        l.addnode(i)
    l.display(l.head)
    sorted_list = MergerSort().sort(l)
    sorted_list.display(sorted_list.head)