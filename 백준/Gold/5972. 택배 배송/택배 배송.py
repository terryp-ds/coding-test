from heapq import *
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
for _ in range(m):
 s,e,w=map(int,input().split())
 g[s]+=[(w,e)]
 g[e]+=[(w,s)]
v=[10**9]*(n+1)
q=[(0,1)]
while q:
 c,x=heappop(q)
 for a,y in g[x]:
  if a+c<v[y]:
   v[y]=a+c
   heappush(q,(a+c,y))
print(v[n])