n,m=map(int,input().split())
a=[list(input()) for _ in range(n)]
def dfs(i,j):
    s=a[i][j]
    if not s: return 0
    q=[(i,j)]
    d=[(0,1),(1,0)][s=='|']
    while q:
        y,x=q.pop()
        a[y][x]=0
        ny,nx=y+d[0],x+d[1]
        if ny>=n or nx>=m: continue
        if s!=a[ny][nx]: break
        q+=[(ny,nx)]
    return 1
print(sum([dfs(i,j) for i in range(n) for j in range(m)]))