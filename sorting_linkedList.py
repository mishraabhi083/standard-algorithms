class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head, self.tail = None, None

    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def sort_list(self):
        temp_outer = self.head
        while temp_outer:
            temp_inner = self.head
            while temp_inner.next:
                if temp_inner.val <= temp_inner.next.val:
                    temp_inner.val, temp_inner.next.val = temp_inner.next.val, temp_inner.val
                temp_inner = temp_inner.next
            temp_outer = temp_outer.next
        return self.head

    def makeEnd(self, node):
        if node:
            trash = node.next
            node.next = None
            del trash

    def merge_sort(self, linked_list):
        print(linked_list)

        def merge(list1, list2):
            first_pointer = list1.head
            second_pointer = list2.head
            result_list = LinkedList()
            while first_pointer or second_pointer:
                if first_pointer.val <= second_pointer.val:
                    result_list.add_node(first_pointer.val)
                    trash = first_pointer
                    first_pointer = first_pointer.next
                    del trash
                else:
                    result_list.add_node(second_pointer.val)
                    trash = second_pointer
                    second_pointer = second_pointer.next
                    del second_pointer

            while first_pointer:
                result_list.add_node(first_pointer.val)
                first_pointer = first_pointer.next

            while second_pointer:
                result_list.add_node(second_pointer)
                second_pointer = second_pointer.next
            return result_list

        def list_bisector(linked_list):
            head = linked_list.head
            if (head == None):
                return head

            slow = head
            fast = head

            while (fast.next != None and fast.next.next != None):
                slow = slow.next
                fast = fast.next.next

            linked_list.makeEnd(slow)
            list1 = linked_list
            list2 = LinkedList()
            tmp = slow.next
            while tmp:
                list2.add_node(tmp.val)
                tmp = tmp.next
            return (list1, list2)

        if (not linked_list.head )or (not linked_list.head.next):
            return LinkedList
        else:
            l1, l2 = list_bisector(linked_list)
            return merge(self.merge_sort(l1), self.merge_sort(l2))

    def __str__(self):
        s = ""
        temp = self.head
        while temp:
            s += f"{temp.val} -> "
            temp = temp.next
        return s


if __name__ == "__main__":
    l = LinkedList()
    for i in range(11, 1, -1):
        l.add_node(i)
    print(l)
    l.merge_sort(l)
    print(l)