def counterDiagonal(mat, n):
  # Write your code here
  for col in range(n):
    i = 0;j = col
    while (j >= 0 and i < n):
      print(mat[i][j],end=' ')
      j-=1
      i+=1
  for row in range(1,n):
    i = row;j = n - 1
    while (i < n and j >= 0):
      print(mat[i][j],end=' ')
      j-=1
      i+=1