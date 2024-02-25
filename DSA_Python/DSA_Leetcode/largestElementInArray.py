class LargestElement:
    def __init__(self, arr):
        self.arr = arr

    def largestElement(self, arr, n) -> int:
        arr.sort()
        print(arr)
        return arr[-1]
    
if __name__ == "__main__":
    arr = [1, 5, 10, 7, 0, 6]
    le = LargestElement(arr)
    largest = le.largestElement(arr, 6)
    print(largest)
