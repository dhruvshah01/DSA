class LowerBound:
    def __init__(self) -> None:
        pass

    def search(self, arr, n, x):
        low = 0
        high = n-1
        idx = -1
        if x > arr[-1]:
            return len(arr) 
        while low <= high:
            mid = (low+high)//2
            if arr[mid] >= x:
                idx = mid
                high = mid - 1
            else: 
                low = mid + 1
        return idx


if __name__ == "__main__":
    lb = LowerBound()
    arr = [1, 2, 3, 4, 5, 6, 7]
    x = 3
    print(lb.search(arr, len(arr), x))