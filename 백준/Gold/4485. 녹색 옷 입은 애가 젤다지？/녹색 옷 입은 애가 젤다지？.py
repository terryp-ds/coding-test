from heapq import *
import sys
input=sys.stdin.readline
i=1
while 1:
    n=int(input())
    if not n: break
    a=[[*map(int,input().split())] for _ in range(n)]
    v=[[10**6]*n for _ in range(n)]
    q=[(a[0][0],0,0)]
    v[0][0]=a[0][0]
    dy,dx=[1,-1,0,0],[0,0,1,-1]
    while q:
        c,y,x=heappop(q)
        for j in range(4):
            ny,nx=y+dy[j],x+dx[j]            
            if 0<=ny<n and 0<=nx<n:
                nc=c+a[ny][nx]
                if v[ny][nx]>nc:
                    v[ny][nx]=nc
                    heappush(q,(nc,ny,nx))
    print(f'Problem {i}: {v[n-1][n-1]}')
    i+=1