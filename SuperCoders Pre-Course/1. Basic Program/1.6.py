n = int(input())  
# This will print the rows  
for i in range(1, n+1):  
    # This will print number of column  
    for j in range(i, 1,-1):
      print(j, end='')
    for j in range(1,i+1):
      print(j,end='')
    print("")