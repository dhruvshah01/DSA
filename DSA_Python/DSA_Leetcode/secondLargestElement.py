import sys
class SecondLargest:
    def __init__(self):
        pass
    def getSecondOrderElements(self, n: int,  a) -> [int]:
        
        minimum = sys.maxsize
        maximum = -minimum

        secondMinimum = minimum - 1
        secondMaximum = maximum + 1

        for i in range(n):
            if (a[i] < minimum):
               minimum = a[i]
            if (a[i] > maximum):
                maximum = a[i]
        
        print(minimum)
        print(maximum)

        for i in range(n):
            if (a[i] < secondMinimum and a[i] != minimum):
                secondMinimum = a[i]
            if (a[i] > secondMaximum and a[i] != maximum):
                secondMaximum = a[i]

        print(secondMinimum, secondMaximum)

        return [secondMinimum, secondMaximum]
    
if __name__ == "__main__":
    arr = [1, 5, 10, 7, 0, 6]
    sl = SecondLargest()
    second_order_elements = sl.getSecondOrderElements(len(arr), arr)
    print("Second Order Elements:", second_order_elements)

             