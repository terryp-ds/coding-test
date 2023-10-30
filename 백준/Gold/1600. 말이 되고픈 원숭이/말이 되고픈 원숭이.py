from collections import deque
import sys
input=sys.stdin.readline
k=int(input())
w,h=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
v=[[[0]*(k+1) for _ in range(w)] for _ in range(h)]
dy,dx=[1,-1,0,0,2,2,1,1,-1,-1,-2,-2],[0,0,1,-1,-1,1,-2,2,-2,2,-1,1]
q=deque([(0,0,0)])
v[0][0][0]=1
while q:
    y,x,c=q.popleft()
    if (y,x)==(h-1,w-1): break
    for i in range(12):
        ny,nx,nc=y+dy[i],x+dx[i],c+(i>3)
        if i>3 and c>=k: break
        if 0<=ny<h and 0<=nx<w and not v[ny][nx][nc] and not a[ny][nx]:
            q.append((ny,nx,nc))
            v[ny][nx][nc]=v[y][x][c]+1
if v[h-1][w-1][c]: print(v[h-1][w-1][c]-1)
else: print(-1)