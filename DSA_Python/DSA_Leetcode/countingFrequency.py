def countFrequency(arr, n, x):
    hash = {}
    j = 1
    for i in range(n):
        if arr[j] in hash and j <= x:
            hash[arr[j]]+=1
            j+=1
        elif j <= x:
            hash[arr[i]] = 0
            j+=1
    
    return list(hash.values())
    

if __name__ == "__main__":
    arr = [11, 14, 8, 3, 12, 14, 1, 7, 4, 3]    
    x = countFrequency(arr, len(arr), 14)
    print(x)   