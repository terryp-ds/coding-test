import sys
input=sys.stdin.readline

for i in range(int(input())):
    m,n,k=map(int, input().split())
    c=[list(map(int,list(input().split()))) for _ in range(k)]
    g=[[0]*m for _ in range(n)]

    for x,y in c:
        g[y][x]=1

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    v=[[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if g[i][j] and not v[i][j]:
                s=[(i,j)]

                while s:
                    y,x=s.pop()
                    v[y][x]=i*m+j+1

                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]

                        if 0<=nx<m and 0<=ny<n and g[ny][nx] and not v[ny][nx]:
                            s.append((ny,nx))

    print(len(set([i for j in v for i in j])-set([0])))
