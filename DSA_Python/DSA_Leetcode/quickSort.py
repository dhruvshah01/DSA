class QuickSort:
    def __init__(self, arr):
        self.arr = arr
    
    def partition(self, arr, low, high):
        part = arr[low]
        i = low
        j = high
        while (i < j):
            while (arr[i] < part & i < high):
                i = i+1
            while (arr[j] > part & j > low):
                j = j-1
        
            if (i < j):
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j
    
    def qsort(self, arr, low, high):
        if (low < high):
            p = partition(arr, low, high)
            qsort(arr, low, p-1)
            qsort(arr, p+1, high)

if __name__ == "__main__":
    arr = [10, 8, 13, 2, 9]
    Q = QuickSort(arr)
    Q.partition(arr, 0, len(arr)-1)
    print(arr)


