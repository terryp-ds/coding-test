import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    s,e=map(int,input().split())
    g[s]+=[e]
    g[e]+=[s]

d=[[0,0] for _ in range(n+1)]
v=[0]*(n+1)

def dfs(c):
    v[c]=1
    d[c][1]=1
    for x in g[c]:
        if not v[x]:
            dfs(x)
            d[c][0]+=d[x][1]
            d[c][1]+=min(d[x])

dfs(1)
print(min(d[1]))
