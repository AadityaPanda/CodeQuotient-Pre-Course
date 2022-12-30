def power(n, e):
    if e < 0:
        return -1
    elif e == 0:
        return 1
    else:
        return (n*power(n, e-1))