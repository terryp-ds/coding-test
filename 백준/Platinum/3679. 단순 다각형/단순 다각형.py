def ccw(a,b,c): return ((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))>=0
def convex_hull(p):
    s=[]
    for c in p:
        while len(s)>1:
            a,b=s[-2:]
            if ccw(a,b,c): break
            s.pop()
        s.append(c)
    return s
for _ in range(int(input())):
    n,*a=[*map(int,input().split())]
    a=sorted(zip(a[::2],a[1::2],range(n)))
    c=[i[2] for i in convex_hull(a)]
    s=set(c)
    for i in range(n-1,-1,-1):
        if a[i][2] not in s: c+=[a[i][2]]
    print(*c)