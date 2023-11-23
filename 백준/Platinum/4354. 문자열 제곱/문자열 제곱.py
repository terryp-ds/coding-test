while 1:
    p=input()
    if p=='.':break
    m=len(p)
    a=[0]*m
    n,i=0,1
    while i<m:
        if p[i]==p[n]:
            n+=1
            a[i]=n
            i+=1
        else:
            if n: n=a[n-1]
            else:
                a[i]=0
                i+=1
    l=m-a[-1]
    print([m//l,1][m%l>0])