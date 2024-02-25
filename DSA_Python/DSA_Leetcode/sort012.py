class sort:
    def __init__(self) -> None:
        pass
    def sort012(self, arr, n) :

        # write your code here
        # don't return anything
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            if (arr[i] == 0):
                cnt0 = cnt0+1
            elif (arr[i] == 1):
                cnt1 = cnt1+1
            else:
                cnt2 = cnt2+1
        for i in range(0, cnt0, 1):
            arr[i] = 0

        for i in range(cnt0, cnt0+cnt1, 1):
            arr[i] = 1   

        for i in range(cnt1+cnt0, cnt1+cnt2+cnt0, 1):
            arr[i] = 2

if __name__ == "__main__":
    s = sort()
    arr = [1, 1, 2, 0, 0]
    s.sort012(arr, len(arr))
