class longestSequence:
    def __init__(self) -> None:
        pass

    def sequence(self, arr, n):
        arr.sort()
        cnt = 1
        longest = 1
        for i in range(n-1):
            if (arr[i+1] == arr[i]+1):
                print(arr[i])
                cnt+=1
            elif (arr[i+1] == arr[i]):
                cnt = cnt
            else:
                cnt = 1
            longest = max(cnt, longest)    
        print(arr)
        return longest
    
if __name__ == "__main__":
    l = longestSequence()
    arr = [15, 6, 2, 1, 16, 4, 2, 29, 9, 12, 8, 5, 14, 21, 8, 12, 17, 16, 6, 26, 3]
    
    print(l.sequence(arr, len(arr)))
