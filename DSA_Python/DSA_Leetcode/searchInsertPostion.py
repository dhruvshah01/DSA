def search(arr, m):
    low = 0
    high = len(arr) - 1
    idx = len(arr)
    while low <= high:
        mid = (low+high)//2
        if (arr[mid] >= m):
            idx = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return idx


if __name__ == "__main__":
    arr =  [1, 2, 4, 7]
    m = 6
    print(search(arr, m))