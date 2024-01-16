import sys
input=sys.stdin.readline
n,m=map(int,input().split())
f=float('inf')
v=[[f]*(n+1) for _ in range(n+1)]
for _ in range(m):
 s,e,w=map(int,input().split())
 v[s][e]=w
for m in range(n+1):
 for s in range(n+1):
  for e in range(n+1):
   v[s][e]=min(v[s][e],v[s][m]+v[m][e])
m=f
for i in range(1,n+1):m=min(m,v[i][i])
print(-1 if m==f else m)