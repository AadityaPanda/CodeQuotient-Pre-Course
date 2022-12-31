def find_first_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(arr) and arr[low] == x:
        return low
    else:
        return -1

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = find_first_occurrence(arr, K)
    print(result)