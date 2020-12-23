class complex_number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary


class complex_node(complex_number):
    def __init__(self, real, imaginary):
        super().__init__(real, imaginary)
        self.next = None

    def __le__(self, other):
        def distance_from_origin(real, imaginary):
            return (real**2 + imaginary**2)**0.5

        return distance_from_origin(self.real,
                                    self.imaginary) < distance_from_origin(
                                        other.real, other.imaginary)

    def __gt__(self, other):
        def distance_from_origin(real, imaginary):
            return (real**2 + imaginary**2)**0.5

        return distance_from_origin(self.real,
                                    self.imaginary) >= distance_from_origin(
                                        other.real, other.imaginary)


class LinkedList:
    def __init__(self):
        self.head, self.tail = None, None

    def add_node(self, real, imaginary):
        if not self.head:
            self.head = complex_node(real, imaginary)
            self.tail = self.head
        else:
            self.tail.next = complex_node(real, imaginary)
            self.tail = self.tail.next

    def sort_list(self):
        # def swap_node(node1,node2): #only vailid for consicutive node swapping

        temp_outer = self.head
        while temp_outer:
            temp_inner = self.head
            while temp_inner.next:
                if temp_inner > temp_inner.next:
                    temp_inner.real, temp_inner.next.real = temp_inner.next.real, temp_inner.real
                    temp_inner.imaginary, temp_inner.imaginary = temp_inner.next.imaginary, temp_inner.imaginary
                temp_inner = temp_inner.next
            temp_outer = temp_outer.next
        return self.head

    def __str__(self):
        s = ""
        temp = self.head
        while (temp):
            s += f"{temp.real}+{temp.imaginary}i --> "
            temp = temp.next
        return s


if __name__ == "__main__":
    l = LinkedList()
    l.add_node(1, 2)
    l.add_node(2, 3)
    l.add_node(3, 4)
    l.add_node(-1, -2)
    print(l)
    l.sort_list()
    print("after sorting :-")
    print(l)