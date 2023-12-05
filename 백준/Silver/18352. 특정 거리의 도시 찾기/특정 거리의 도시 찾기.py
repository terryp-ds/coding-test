from collections import *
import sys
input=sys.stdin.readline
n,m,k,x=map(int,input().split())
g=[[] for _ in range(n+1)]
for _ in range(m):
 s,e=map(int,input().split())
 g[s]+=[e]
v=[10**11]*(n+1)
q=deque([x])
v[x]=0
while q:
 c=q.popleft()
 for x in g[c]:
  if v[c]+1<v[x]: 
   v[x]=v[c]+1
   q+=[x]
a=[i for i in range(n+1) if v[i]==k]
print(*[[-1],a][bool(a)],sep='\n')