n=int(input())
list1 = list(int(num) for num in input().strip().split())[:n]
removedup=set(list1)
afterremovedup=list(removedup)
afterremovedup.sort()
if len(afterremovedup)>1:
    print(afterremovedup[-2])
else:
    print("0")