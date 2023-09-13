from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[[*map(int,input().rstrip())] for _ in range(n)]
v=[[0]*m for _ in range(n)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]

q=deque([(0,0)])
v[0][0]=1

while q:
    y,x=q.popleft()
    
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]

        if 0<=ny<n and 0<=nx<m and a[ny][nx] and not v[ny][nx]:
            q.append((ny,nx))
            v[ny][nx]=v[y][x]+1

print(v[-1][-1])