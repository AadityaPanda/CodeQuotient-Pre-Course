def removeDuplicates(arr,n):
    i = 1;j = 1
    while (i < n):
        if (arr[i] != arr[i-1]):
            arr[j] = arr[i]
            j+=1
        i+=1
    return arr[0:j]