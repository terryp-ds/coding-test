import heapq
import sys
input=sys.stdin.readline
m,n=map(int,input().split())
a=[[*map(int,list(input().rstrip()))] for _ in range(n)]
v=[[1e6]*m for _ in range(n)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]

q=[(0,0,0)]
v[0][0]=0

while q:
    w,y,x=heapq.heappop(q)

    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]

        if 0<=ny<n and 0<=nx<m:
            c=w+a[ny][nx]

            if c<v[ny][nx]:
                v[ny][nx]=c
                heapq.heappush(q,(c,ny,nx))

print(v[-1][-1])