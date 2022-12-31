def partitionArray(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        while arr[left] < x:
            left += 1
        while arr[right] > x:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr