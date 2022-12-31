def rotationCount(a: list[int]) -> int:
  size = len(a)
  for i in range(1, size):
    if a[i] < a[i - 1]:
      return i
  return 0