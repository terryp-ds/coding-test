from heapq import *
import sys
input=sys.stdin.readline
f=float('inf')
for _ in range(int(input())):
    n,d,c=map(int,input().split())
    g=[[] for _ in range(n+1)]
    v=[f]*(n+1)
    for _ in range(d):
        a,b,s=map(int,input().split())
        g[b]+=[(s,a)]
    q=[(0,c)]
    v[c]=0
    n=1
    while q:
        w,c=heappop(q) 
        for (a,x) in g[c]:
            t=w+a
            if t<v[x]:
                if v[x]==f: n+=1
                heappush(q,(t,x))
                v[x]=t
    print(*(n,max([i for i in v if i!=f])))
