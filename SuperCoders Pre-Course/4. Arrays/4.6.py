def reverseSubarray(arr, N, K):
    for i in range(0, len(arr),K):
        l=arr[i:i+K]
        l.reverse()
        arr[i:i+K] =l
    return arr