a=[[*map(int,input().split())] for _ in range(9)]
z=[]
for i in range(9):
    for j in range(9):
        if not a[i][j]: z.append((i,j))

def row(y,n):
    for x in range(9):
        if n == a[y][x]: return 0
    return 1

def col(x,n):
    for y in range(9):
        if n == a[y][x]: return 0
    return 1

def sq(y,x,n):
    r,c=y-y%3,x-x%3
    for i in range(3):
        for j in range(3):
            if a[r+i][c+j]==n: return 0
    return 1

def dfs(i):
    if i==len(z):
        print(*[' '.join(map(str,r)) for r in a], sep='\n')
        exit(0)
    y,x=z[i]
    for j in range(1,10):
        if row(y,j) and col(x,j) and sq(y,x,j):
            a[y][x]=j
            dfs(i+1)
            a[y][x]=0

dfs(0)