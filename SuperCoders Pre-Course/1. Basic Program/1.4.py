def fib_sequence(n):
    if (n<0):
        print ("Enter a positive number")
    else:
        f1, f2 = 0, 1
    if n == 1:
        print (f1)
    elif n == 2:
        print (f1)
        print (f2)
    else:
        print (f1)
        print (f2)
        for i in range (3, n+1):
            f3 = f1 + f2
            print (f3)
            f1 = f2
            f2 = f3