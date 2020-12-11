import math as m
class Heap:
    def __init__(self):
        self.data=[]
    def addNode(self,value):
        self.data.append(value)
        index=len(self.data)-1
        while index!=0:
            if self.data[index] < self.data[m.floor((index-1)//2)]:
                self.data[index] , self.data[m.floor((index-1)//2)] =  self.data[m.floor((index-1)//2)] , self.data[index] 
                #swap
            index=m.floor((index-1)//2)
        return True
    def display(self):
        print(self.data)
    def heapify(self,index):
        if index < len(self.data):
            if (index*2)+1 < len(self.data):
                if self.data[index] > self.data[(index*2)+1]:
                    self.data[index] , self.data[(index*2)+1] = self.data[(index*2)+1],self.data[index] 
                    self.heapify((index*2)+1)
            if (index*2)+2 < len(self.data):
                if self.data[index] > self.data[(index*2)+2]:
                    self.data[index] , self.data[(index*2)+2] = self.data[(index*2)+2],self.data[index] 
                    self.heapify((index*2)+2)
    def extractMin(self):
        self.data[0],self.data[len(self.data)-1]=self.data[len(self.data)-1],self.data[0]
        min_value_so_far=self.data.pop(-1)
        self.heapify(0)
        return min_value_so_far
    def heapsort(self):
        sorted=[]
        while self.data!=[]:
            sorted.append(self.extractMin())
        return sorted
if __name__ == '__main__':
    main_heap=Heap()
    for i in [17,3,15,25,12,1,4]:
        main_heap.addNode(i)
    print("heap is : ")
    main_heap.display()
    sorted = main_heap.heapsort()
    print('sorted data :',sorted)


    
