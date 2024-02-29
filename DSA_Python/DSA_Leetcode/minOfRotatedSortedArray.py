import sys
class RotatedSortedArray:
    def __init__(self) -> None:
        pass

    def minSortedArray(self, arr):
        n = len(arr)
        high = n - 1
        low = 0
        min_val = sys.maxsize
        while (low <= high):
            mid = (low+high)//2
            if (arr[mid] >= arr[low]):
                min_val = min(min_val, arr[low])
                low = mid + 1
            else:
                min_val = min(min_val, arr[mid])
                high = mid - 1
        
        return min_val
    
if __name__ == "__main__":
    r = RotatedSortedArray()
    arr = [4, 5, 6, 7, 1, 2, 3]
    print(r.minSortedArray(arr))
