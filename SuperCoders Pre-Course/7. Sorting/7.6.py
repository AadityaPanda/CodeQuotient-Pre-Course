def reduceArray(arr):
    c=list(arr)
    d=[]
    for l in range(0,len(c)):
        b=min(c)
        e=0
        for j in range(len(c)):
            c[j]=c[j]-b
            e+=1
        c=list(filter(lambda x:x!=0,c))
        d.append(e)
        if len(c)==0:
            return(d)