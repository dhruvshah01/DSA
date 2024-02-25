class ShiftArrayByK:
    def __init__(self) -> None:
        pass

    def shift(self, arr, n, k) -> [int]:
        tmp = arr.copy()
        x = 0
        y = 0
        for i in range(k, n, 1):
            print(i)
            arr[x] = tmp[i]
            x = x+1
        
        print(arr)

        for i in range(k):
            arr[x] = tmp[i]
            x = x+1          

        return arr

if __name__ == "__main__":
    s = ShiftArrayByK()
    arr = [1, 2, 3 , 4, 6]
    k = 2
    n = len(arr)
    tmp = s.shift(arr, n, k)
    print(tmp)
