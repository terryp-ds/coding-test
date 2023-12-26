import sys
input=sys.stdin.readline
def dfs(i):
    if v[i]: return 0
    v[i]=1
    for x in g[i]:
        if not s[x] or dfs(s[x]): 
            s[x]=i
            return 1
    return 0
n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
for i in range(n):
    e=[*map(int,input().split())][1:]
    g[i+1]+=e
s=[0]*(m+1)
for i in range(1,n+1):
    v=[0]*(n+1)
    dfs(i)
print(len([i for i in s if i]))