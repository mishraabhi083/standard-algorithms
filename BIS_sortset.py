class BubbleSort:
    def __init__(self, comaparator):
        self.comaparator = comaparator
    def sort(self, arr, reversed=False):
        for i in range(len(arr)):
            flag = 0
            for j in range(len(arr) - 1):
                if not reversed:
                    if self.comaparator(arr[j], arr[j + 1]) > 0:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]  #swap action
                        flag = 1
                else:
                    if self.comaparator(arr[j], arr[j + 1]) < 0:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]  #swap action
                        flag = 1
            if not flag:
                return arr
        return arr


class InsertionSort:
    def __init__(self, comaparator):
        self.comaparator = comaparator
    def sort(self, arr, reversed=False):
        for i in range(1,len(arr)):
            for j in range(i,0,-1):
                if not reversed:
                    if self.comaparator(arr[j-1], arr[j]) > 0:
                        arr[j-1], arr[j] = arr[j], arr[j-1]  #swap action
                else:
                    if self.comaparator(arr[j-1], arr[j]) < 0:
                        arr[j-1], arr[j] = arr[j], arr[j-1]  #swap action
        return arr

class SelectionSort:
    def __init__(self,comaparator):
        self.comaparator=comaparator
    def sort(self, arr, reversed=False):
        for i in range(len(arr) - 1):
            flag = 0
            for j in range(i + 1, len(arr)):
                if not reversed:
                    if self.comaparator(arr[i], arr[j]) > 0:
                        arr[i], arr[j] = arr[j], arr[i]  #swap action
                        flag = 1
                else:
                    if self.comaparator(arr[i], arr[j]) < 0:
                        arr[i], arr[j] = arr[j], arr[i]  #swap action
                        flag = 1
            if not flag:
                return arr
        return arr

        
if __name__ == "__main__":

    '''
        In this example all the sorting engines are set to sort simple intiger dataset
        but it can be changed by changing the comparator functions as argument.
    '''

    arr = list(map(int, input("Enter dataset : ").strip().split()))
    sort_engine = BubbleSort(lambda x, y: x - y)
    print('from bubble sorted : ', sort_engine.sort(arr))
    sort_engine = InsertionSort(lambda x, y: x - y)
    print('from Insertion sorted : ', sort_engine.sort(arr,reversed=True))
    sort_engine = SelectionSort(lambda x, y: x - y)
    print('from Selection sorted : ', sort_engine.sort(arr))
