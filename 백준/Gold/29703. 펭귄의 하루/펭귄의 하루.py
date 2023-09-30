from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[input().rstrip() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j]=='S': sy,sx=i,j
        if a[i][j]=='H': hy,hx=i,j

q=deque([(sy,sx,0)])

dy=[1,-1,0,0]
dx=[0,0,1,-1]

v=[[[0,0] for _ in range(m)] for _ in range(n)]
v[sy][sx][0]=1

while q:
    i,j,f=q.popleft()
    if a[i][j]=='H' and f: break
    p=v[i][j][f]

    for k in range(4):
        ny=i+dy[k]
        nx=j+dx[k]

        if 0<=ny<n and 0<=nx<m and not v[ny][nx][f]:
            c=a[ny][nx]
            if c!='D':
                if not f and c=='F':
                    q.append((ny,nx,1))
                    v[ny][nx][1]=p+1
                else:
                    q.append((ny,nx,f))
                v[ny][nx][f]=p+1

print(v[hy][hx][1]-1 if (i,j,f)==(hy,hx,1) else -1)