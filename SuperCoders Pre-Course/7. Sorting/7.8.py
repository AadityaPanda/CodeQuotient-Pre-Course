def maxToys(array,n,sum):
  array.sort()
  count = 0
  for i in array:
    if sum >= i:
      count +=1
      sum -= i
    else:
      break
  return count