from collections import deque
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
a=[[*map(int,list(input().strip()))] for _ in range(n)]
v=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]
q=deque([(0,0,0)])
v[0][0][0]=1
dy,dx=[1,-1,0,0],[0,0,1,-1]
while q:
    y,x,d=q.popleft()
    if (y,x)==(n-1,m-1): break
    c=v[y][x][d]
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if not (0<=ny<n and 0<=nx<m): continue
        if not v[ny][nx][d] and not a[ny][nx]:
            q.append((ny,nx,d))
            v[ny][nx][d]=c+1
        if d<k and not v[ny][nx][d+1] and a[ny][nx]:
            q.append((ny,nx,d+1))
            v[ny][nx][d+1]=c+1
t=v[n-1][m-1][d]
print(t if t else -1)
