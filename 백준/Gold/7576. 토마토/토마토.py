import sys
input=sys.stdin.readline
m,n=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(n)]
q=[(y,x) for x in range(m) for y in range(n) if a[y][x]==1]
dy,dx=[1,-1,0,0],[0,0,1,-1]
d=0
while q:
    nq=[]
    for y,x in q:
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if not (0<=ny<n and 0<=nx<m) or a[ny][nx]: continue
            a[ny][nx]=1
            nq.append((ny,nx))
    if nq:d+=1
    q=nq
print([d,-1][bool(sum([r.count(0) for r in a]))])