from collections import deque
n,m=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(n)]
v=[[0]*m for _ in range(n)]
for i in range(n):
    if 2 in a[i]:
        j=a[i].index(2)
        break
q=deque([(i,j)])
dy,dx=[1,-1,0,0],[0,0,1,-1]
while q:
    y,x=q.popleft()
    for k in range(4):
        ny,nx=y+dy[k],x+dx[k]
        if not (0<=ny<n and 0<=nx<m) or not a[ny][nx] or v[ny][nx]: continue
        v[ny][nx]=v[y][x]+1
        q+=[(ny,nx)]
v[i][j]=0

for i in range(n):
    for j in range(m):
        if not v[i][j] and a[i][j]==1: v[i][j]=-1

for r in v: print(*r)