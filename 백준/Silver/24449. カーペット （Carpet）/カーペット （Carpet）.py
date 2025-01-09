from collections import deque
import sys
input=sys.stdin.readline
h,w=map(int,input().split())
a=[list(input().strip()) for _ in range(h)]
v=[[0]*w for _ in range(h)]
q=deque([(0,0)])
v[0][0]=1
dy,dx=[0,0,1,-1],[1,-1,0,0]
while q:
 y,x=q.popleft()
 for i in range(4):
  m,n=y+dy[i],x+dx[i]
  if 0<=m<h and 0<=n<w and not v[m][n] and a[m][n]!=a[y][x]:
   v[m][n]=v[y][x]+1
   q+=[(m,n)]
z=v[h-1][w-1]
print(z-1 if z else -1)