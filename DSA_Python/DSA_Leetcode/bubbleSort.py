class Sorting:
    def __init__(self, arr):
        self.arr = arr
        
    def bubbleSort(self, arr):
        for i in range(len(arr)-1, 0, -1):
            for j in range(0, i):
                print(j)
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

if __name__ == "__main__":
    arr = [5, 10, 7, 0, 1]
    s = Sorting(arr)
    sorted = s.bubbleSort(arr)
    print(sorted)1
    
