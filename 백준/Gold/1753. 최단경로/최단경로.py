from heapq import *
import sys
input=sys.stdin.readline
f=float('inf')
n,m=map(int,input().split())
k=int(input())
g=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w=map(int,input().split())
    g[s]+=[(w,e)]
v=[f]*(n+1)
v[k]=0
q=[(0,k)]
while q:
    w,c=heappop(q)
    for a,x in g[c]:
        if w+a<v[x]:
            v[x]=w+a
            heappush(q,(w+a,x))
for i in v[1:]: print(i if i<f else 'INF')