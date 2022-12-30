def leftRotate(arr,temp,n,R):
  for i in range(n):
    temp[i] = arr[(i+R)%n];
if __name__ == "__main__":
  x = int(input())
  for _ in range(x):
    n = int(input())
    arr = list(int(num) for num in input().strip().split())
    R = int(input())
    temp = [0]*n
    leftRotate(arr, temp, n, R)
    print(' '.join(str(x) for x in temp))