def rotate_90_degrees(arr, n):
  rotated = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      rotated[i][j] = arr[n - j - 1][i]

  for row in rotated:
    print(' '.join(map(str, row)))
  print()

t = int(input())
for _ in range(t):
  n = int(input())
  arr = []
  for _ in range(n):
    arr.append(list(map(int, input().split())))
  rotate_90_degrees(arr, n)