import math


class Heap:
    def __init__(self):
        self.data = ['x']

    def insertData(self, value):
        self.data.append(value)
        index = len(self.data) - 1
        while index != 1:
            if self.data[math.floor((index - 1) // 2)] > self.data[index]:
                self.data[index], self.data[math.floor(
                    (index - 1) // 2)] = self.data[math.floor(
                        (index - 1) // 2)], self.data[index]
            index = math.floor((index - 1) // 2)

    def heapify(self, index):
        if index < len(self.data):
            if (index * 2) + 1 < len(self.data):
                if self.data[index] > self.data[(index * 2) + 1]:
                    self.data[index], self.data[(index * 2) + 1] = self.data[
                        (index * 2) + 1], self.data[index]
                    self.heapify((index * 2) + 1)
            if (index * 2) + 2 < len(self.data):
                if self.data[index] > self.data[(index * 2) + 2]:
                    self.data[index], self.data[(index * 2) + 2] = self.data[
                        (index * 2) + 2], self.data[index]
                    self.heapify((index * 2) + 2)

    def displayData(self):
        print(self.data)

    def extractMin(self):
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        min_element = self.data.pop(-1)
        self.heapify(1)
        return min_element


if __name__ == "__main__":
    h = Heap()
    for i in [30, 35, 10, 28, 5, 15]:
        h.insertData(i)
    h.displayData()
    h.extractMin()
    h.displayData()

# resource links to read :
# https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate
# https://docs.python.org/3/library/heapq.html