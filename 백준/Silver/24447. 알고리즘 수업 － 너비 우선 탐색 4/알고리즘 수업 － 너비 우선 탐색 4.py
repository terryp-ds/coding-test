from collections import deque
import sys
input=sys.stdin.readline
n,m,r=map(int,input().split())
g=[[] for _ in range(n+1)]
for _ in range(m):
 s,e=map(int,input().split())
 g[s]+=[e]
 g[e]+=[s]
v,d=[0]*(n+1),[-1]*(n+1)
i,v[r],d[r]=1,1,0
q=deque([r])
while q:
 c=q.popleft()
 for x in g[c]:
  if v[x]:continue
  v[x]=i+1
  d[x]=d[c]+1
  q+=[x]
  i+=1
print(sum([i*j for i,j in zip(v,d)]))