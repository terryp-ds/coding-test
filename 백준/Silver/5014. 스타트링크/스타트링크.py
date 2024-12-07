from collections import deque
f,s,g,u,d=map(int,input().split())
q=deque([s])
v=[0]*(f+1)
v[s]=1
while q and not v[g]:
 x=q.popleft()
 for z in [u,-d]:
  if 0<x+z<=f and not v[x+z]:
   q+=[x+z]
   v[x+z]=v[x]+1
print(v[g]-1 if v[g] else 'use the stairs')