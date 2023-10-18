import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
def dfs(y,x):
    if y==m-1 and x==n-1: return 1
    if v[y][x]>-1: return v[y][x]
    c=0
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if 0<=ny<m and 0<=nx<n and a[y][x]>a[ny][nx]: c+=dfs(ny,nx)
    v[y][x]=c
    return c
m,n=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(m)]
v=[[-1]*n for _ in range(m)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
print(dfs(0,0))