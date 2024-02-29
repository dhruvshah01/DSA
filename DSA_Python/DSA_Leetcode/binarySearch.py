def search(nums: [int], target: int):
    # write your code logic !!
    pivot = int(target/2)
    idx = -1
    print(pivot)
    if nums[pivot] == target:
        return pivot
    elif nums[pivot] < target:
        for i in range(1, pivot, 1):
            if (nums[i] == target):
                idx = i
    elif nums[pivot] > target:
        for i in range(pivot, len(nums), 1):
            if (nums[i] == target):
                idx = i
    
    return idx
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 9
    print(search(arr, target))
