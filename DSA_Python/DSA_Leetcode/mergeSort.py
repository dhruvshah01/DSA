class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge(self, arr, low, high):
        if (low >= high):
            return
        mid = (low+high)/2
        merge(arr, low, mid)
        merge(arr, mid+1, high)
        mergeSort(arr, low, mid, high)

    def mergeSort(self, arr, low, mid, high):
        left = low
        right = mid+1

        temp = []
        while (left <= mid & right <= high):
            if (arr[left] < arr[right]):
                temp.add(arr[left])
                left = left+1
            else:
                temp.add(arr[right])
                right = right+1

        while (left <= mid):
            temp.add(arr[left])
            left = left+1

        while (right <= high):
            temp.add(arr[right])
            right = right+1
        
        for i in range(low, high, 1):
            arr[i] = temp[i-low]

if __name__ == "__main__":
    arr = [5, 10, 0, 9, 7]
    m = MergeSort(arr)
    m.merge(arr, 0, len(arr))
    print(arr)


