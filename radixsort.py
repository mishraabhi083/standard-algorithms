class RadixSort:
    def __init__(self):
        self.dataset=[]
    def __prefix_sum(self,arr): # optimization done!
        for i in range(len(arr)):
            arr[i]+=arr[i-1]
        return arr
    def __create_counter(self,arr):
        self.dataset=[i for i in range(len(max(arr)))]
        for i in arr:
            self.dataset[arr]+=1
        self.dataset=self.__prefix_sum(arr)
    def __rearange(dataset,arr,x):  
        res=[]
        for i in arr:
            key=(i%10**x+1)//(10**x)
            res[key]=i
        return res
    def sort(self,arr):
        for nth_digit in range(len(str(max(arr)))):

if __name__ == "__main__":
    arr=list(map(int,input('Enter data : ').strip().split()))

