from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[input().strip() for _ in range(n)]
v=[[[0,0] for _ in range(m)] for _ in range(n)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
q=deque([(0,0,0)])
f=0
while q:
    y,x,b=q.popleft()
    if (y,x)==(n-1,m-1): f=1; break
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if not (0<=ny<n and 0<=nx<m): continue
        if a[ny][nx]=='0' and not v[ny][nx][b]:
            v[ny][nx][b]=v[y][x][b]+1
            q.append((ny,nx,b))
        elif a[ny][nx]=='1' and not v[ny][nx][1] and b<1:
            v[ny][nx][1]=v[y][x][f]+1
            q.append((ny,nx,1))
print(v[y][x][b]+1 if f else -1)