import sys
input=sys.stdin.readline
n,m = map(int,input().split())
a = [[*map(int,input().split())] for _ in range(n)]
dy,dx = [1,-1,0,0],[0,0,1,-1]

c,z = 1,0
for i in range(n):
 for j in range(m):
  if a[i][j]!=1: continue
  s = 0
  c += 1
  a[i][j] = c
  stack = [(i,j)]
  while stack:
   y,x = stack.pop()
   s += 1
   for k in range(4):
    ny,nx = y+dy[k],x+dx[k]
    if 0<=ny<n and 0<=nx<m and a[ny][nx]==1:
     a[ny][nx] = c
     stack += [(ny,nx)]
  z = max(s,z)

print(*[c-1,z],sep='\n')