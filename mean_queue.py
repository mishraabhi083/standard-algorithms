from time import sleep as delay
from bisect import insort
DELAY=1

class ProcessSchedular:
    def __init__(self, initial_data):
        self.processData = [] if initial_data == None else sorted(initial_data)

    def scheduleProcess(self, process_value):
        insort(self.processData, process_value)
        print("median so far : ",self.__find_median_so_far())
        print("data after processing : ", self.processData)
        delay(DELAY)

    def __find_median_so_far(self):
        N = len(self.processData)
        if len(self.processData) % 2 == 0:
            return (self.processData[N // 2] +
                    self.processData[(N // 2) + 1]) / 2
        else:
            return self.processData[N // 2]


if __name__ == "__main__":
    PS = ProcessSchedular(
        list(
            map(
                int,
                input('''enter data for process queue initialization
    [intiger values seprated by spaces ]: ''').strip().split())))
    n = int(input("Enter number of dynamic process : "))
    for i in range(n):
        pd = int(input("Enter process data [single intiger value  ] : "))
        PS.scheduleProcess(pd)
