class MergeSort:
    def __init__(self, comparator):
        self.comparator = comparator

    def __merge(self, a1, a2):
        if a1 == []: return a2
        if a2 == []: return a1
        i, j, resultant = 0, 0, []
        while i < len(a1) and j < len(a2):
            if self.comparator(a1[i], a2[j]) <= 0:
                resultant.append(a1[i])
                i += 1
            else:
                resultant.append(a2[j])
                j += 1

        if i < len(a1):
            resultant += a1[i:]
        elif j < len(a2):
            resultant += a2[j:]

        return resultant

    def sort(
            self,
            arr,
    ):
        if len(arr) == 1: return arr
        else:
            return self.__merge(self.sort(arr[:len(arr) // 2]),
                                self.sort(arr[len(arr) // 2:]))


if __name__ == "__main__":
    arr = list(map(int, input("Enter dataset : ").strip().split()))
    sorting_engine = MergeSort(lambda x, y: x - y)
    print("merge sorted : ", sorting_engine.sort(arr))
