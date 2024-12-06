from collections import deque
dy,dx=[1,-1,0,0],[0,0,1,-1]
def bfs(i,j):
 q=deque([(i,j)])
 v=[[0]*c for _ in range(r)]
 v[i][j]=1
 while q:
  y,x=q.popleft()
  for k in range(4):
   ny,nx=y+dy[k],x+dx[k]
   if 0<=ny<r and 0<=nx<c and not v[ny][nx] and g[ny][nx]<=g[y][x]:
    v[ny][nx]=1
    q+=[(ny,nx)]
    if (ny,nx)==(a-1,b-1): break
 return v[a-1][b-1]
for z in range(int(input())):
 r,c=map(int,input().split())
 a,b=map(int,input().split())
 g=[[*map(int,input().split())] for _ in range(r)]
 s=0
 for m in range(r):
  for n in range(c):
   if m in (0,r-1) or n in (0,c-1):
    s+=bfs(m,n)
 print(f'Case #{z+1}: {s}')