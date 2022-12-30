def printSpiral(a, r, c):
  # Write your code here
  top=0
  down=r-1
  left=0
  right=c-1
  dire=0
  while(top<=down and left <= right):
    if(dire==0):
      for i in range(left,right+1):
        print(a[top][i])
      top+=1
    elif(dire==1):
      for i in range(top,down+1):
        print(a[i][right])
      right-=1
    elif(dire==2):
      for i in range(right,left-1,-1):
        #print("down",down,"right",right,i)
        print(a[down][i])
      down-=1
    elif(dire==3):
      for i in range(down,top-1,-1):
        print(a[i][left])
      left+=1
    dire=(dire+1)%4