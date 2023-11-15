for _ in range(int(input())):
    n,*a=[*map(int,input().split())]
    a=sorted(zip(a[::2],a[1::2],range(n)))
    q=[]
    for z in a:
        while len(q)>1:
            x,y=q[-2:]
            if (y[0]-x[0])*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0])>=0: break
            q.pop()
        q+=[z]
    q=[i[2] for i in q]
    s=set(q)
    for i in range(n-1,-1,-1):
        if a[i][2] not in s: q+=[a[i][2]]
    print(*q)