import sys
input=sys.stdin.readline
r,c,t=map(int, input().split())
arr=[[*map(int,input().split())] for _ in range(r)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
for y in range(r):
    if arr[y][0]==-1:
        loc=(y,0)
        break
for _ in range(t):
    arr2=[[0]*c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if arr[y][x]>0:
                cnt=0
                for i in range(4):
                    ny,nx= y+dy[i],x+dx[i]
                    if 0<=ny<r and 0<=nx<c:
                        if arr[ny][nx]!=-1:
                            arr2[ny][nx]+=arr[y][x]//5
                            cnt+=1
                arr2[y][x]+=arr[y][x]-((arr[y][x]//5)*cnt)
            elif arr[y][x]==-1: arr2[y][x] = -1
    y,x = loc
    for i in range(y-1,0,-1): arr2[i][0]=arr2[i-1][0]
    for i in range(y+2, r-1): arr2[i][0]=arr2[i+1][0]
    for i in [0,-1]: arr2[i]=arr2[i][1:]+[0]
    for i in range(y): arr2[i][-1]=arr2[i+1][-1]
    for i in range(r-1,y+1,-1): arr2[i][-1]=arr2[i-1][-1]
    for i in range(y,y+2): arr2[i]=[-1,0]+arr2[i][1:-1]
    arr = arr2
print(sum(map(sum,arr))+2)