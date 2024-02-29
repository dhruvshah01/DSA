class SearchInRotatedArray:
    def __init__(self) -> None:
        pass

    def search(self, arr, n, k):
        low = 0
        high = n - 1
        idx = -1
        while (low <= high):
            mid = (high + low)//2
            if arr[mid] == k:
                idx =  mid
            if arr[low] <= arr[mid]:
                if (arr[mid] >= k and k >= arr[low]):
                    high = mid - 1
                else:
                    low = mid + 1
            elif arr[mid] <= arr[high]:
                if (arr[mid] <= k and k <= arr[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        
        return idx

if __name__ == "__main__":
    s = SearchInRotatedArray()
    arr = [5, 6, 1, 2, 4]
    k = 5
    print(s.search(arr, len(arr), k))



