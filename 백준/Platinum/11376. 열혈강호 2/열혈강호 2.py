import sys
input=sys.stdin.readline
def dfs(i):
 if v[i]:return
 v[i]=1
 for x in g[i//2]:
  if c[x]<0:c[x]=i;return 1
 for x in g[i//2]:
  if dfs(c[x]):c[x]=i;return 1
n,m=map(int,input().split())
g=[[*map(int,input().split())][1:] for _ in range(n)]
c=[-1]*(m+1)
for i in range(2*n):
 v=[0]*2*n
 dfs(i)
print(m+1-c.count(-1))