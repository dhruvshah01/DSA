import sys
class SubArray:
    def __init__(self) -> None:
        pass

    def maxSubArray(self, arr, n) -> int:
        maxi = -sys.maxsize-1
        sum = 0
        for i in range(n):
            sum = sum+arr[i]

            if (sum > maxi):
                maxi = sum

            if (sum < 0):
                sum = 0

        return maxi if maxi > 0 else 0

if __name__ == "__main__":
    m = SubArray()
    arr = [-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16 ,-10]
    print(m.maxSubArray(arr, len(arr)))
    
    