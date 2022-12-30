def moveElements(arr, n):
  for i in range(n):
    key = arr[i]
    if (key >= 0):
      j = i
      while (j > 0):
        if(arr[j-1]<0):
          arr[j-1],arr[j] = arr[j],arr[j-1]
        else:
          break
        j-=1;