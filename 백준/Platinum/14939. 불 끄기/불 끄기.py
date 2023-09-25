import copy
dy,dx=[-1,1,0,0,0],[0,0,-1,1,0]
t=[list(input().strip()) for _ in range(10)]
m=101
def off(y,x,a):
    global c
    for i in range(5):
        ny,nx=y+dy[i],x+dx[i]
        if 0<=nx<10 and 0<=ny<10:
            a[ny][nx]='#' if a[ny][nx]=='O' else 'O'
    c+=1

for f in range(1<<10):
    a=copy.deepcopy(t)
    c=0
    for i in range(10):
        if f & (1<<i):
            off(0,i,a)

    for i in range(1,10):
        for j in range(10):
            if a[i-1][j]=='O': off(i,j,a)

    f=1
    for i in range(10):
        if a[9][i]=='O': f=0

    if f: m=min(c,m)

print(m if m<101 else -1)