import sys
input=sys.stdin.readline
def dfs(s,f):
 v[s]=f
 q=[s]
 while q:
  c=q.pop()
  for x in g[c]:
   if v[x]==0:
    q+=[x]
    v[x]=-v[c]
   elif v[x]==v[c]:return
 return 1
for _ in range(int(input())):
 n,m=map(int,input().split())
 g=[[] for _ in range(n+1)]
 v=[0]*(n+1)
 for _ in range(m):
  s,e=map(int,input().split())
  g[s]+=[e]
  g[e]+=[s]
 i=f=1
 while i<=n:
  if v[i]==0:
   d=dfs(i,f)
   if not d:print('NO');f=0;break
  i+=1
 if f:print('YES')