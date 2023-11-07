import bisect as b
while 1:
    try:
        n=int(input())
        s=[*map(int,input().split())]
        a=[0]*n
        c=[]
        for i in range(n):
            if not c or s[i]>c[-1]:
                c.append(s[i])
                a[i]=len(c)-1
            else:
                a[i]=b.bisect_left(c,s[i])
                c[a[i]]=s[i]
        print(len(c))
    except: break