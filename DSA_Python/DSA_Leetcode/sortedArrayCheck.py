class sortedArrayCheck:
    def __init__(self):
        pass
    def check(self, n, arr) -> bool:
        i = 0
        j = i+1
        flag = False
        for x in range(n-1):
            flag = False
            if (arr[i] <= arr[j]):
                flag = True
                i = i+1
                j = j+1
        
        return flag
    
if __name__ == "__main__":
    s = sortedArrayCheck()
    arr = [0, 1, 2, 3, 4]
    flag = s.check(len(arr), arr)
    print(flag)
    arr = [1, 2, 3, 0]
    flag = s.check(len(arr), arr)
    print(flag)

    