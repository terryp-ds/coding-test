n,m=map(int,input().split())
a=[[*map(int,list(input().strip()))] for _ in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j]=1-a[i][j]

dy,dx=[-1,1,0,0],[0,0,-1,1]
s=set()
d={}
g=2
for i in range(n):
    for j in range(m):
        if not a[i][j]: s.add((i,j))
        elif a[i][j]==1:
            q=[(i,j)]
            a[i][j]=g
            c=1
            while q:
                y,x=q.pop()
                for k in range(4):
                    ny,nx=y+dy[k],x+dx[k]
                    if 0<=ny<n and 0<=nx<m and a[ny][nx]==1:
                        q.append((ny,nx))
                        a[ny][nx]=g
                        c+=1
            d[g]=c
            g+=1

a2=[[0]*m for _ in range(n)]
for (y,x) in s:
    s2=set()
    for k in range(4):
        ny,nx=y+dy[k],x+dx[k]
        if 0<=ny<n and 0<=nx<m and a[ny][nx]:
            s2.add(a[ny][nx])
    a2[y][x]=(1+sum([d[i] for i in s2]))%10

for r in a2:
    print(''.join(map(str,r)))