r,c,t=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(r)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
for y in range(r):
    if a[y][0]==-1: l=(y,0); break
for _ in range(t):
    a2=[[0]*c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if a[y][x]<0: continue
            if a[y][x]==-1: a2[y][x]=-1; continue
            n=0
            for i in range(4):
                ny,nx=y+dy[i],x+dx[i]
                if not (0<=ny<r and 0<=nx<c) or a[ny][nx]==-1: continue
                a2[ny][nx]+=a[y][x]//5
                n+=1
            a2[y][x]+=a[y][x]-((a[y][x]//5)*n)
    y,x=l
    for i in range(y-1,0,-1): a2[i][0]=a2[i-1][0]
    for i in range(y+2,r-1): a2[i][0]=a2[i+1][0]
    for i in [0,-1]: a2[i]=a2[i][1:]+[0]
    for i in range(y): a2[i][-1]=a2[i+1][-1]
    for i in range(r-1,y+1,-1): a2[i][-1]=a2[i-1][-1]
    for i in range(y,y+2): a2[i]=[-1,0]+a2[i][1:-1]
    a=a2
print(sum(map(sum,a))+2)