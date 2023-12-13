from heapq import *
import sys
input=lambda:map(int,sys.stdin.readline().split())
n,m=input()
g=[[] for _ in range(n+1)]
v=[0]*(n+1)
for _ in range(m):
 s,e,w=input()
 g[s]+=[(w,e)]
 g[e]+=[(w,s)]
q=[(0,1)]
i,t=0,0
while q and i<n:
 w,c=heappop(q)
 if not v[c]:
  v[c]=1
  t+=w
  i+=1
  for e in g[c]: heappush(q,e)
print(t)