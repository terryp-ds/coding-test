import sys
input=sys.stdin.readline
n=int(input())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    p,c,w=map(int,input().split())
    g[p].append((w,c))
    g[c].append((w,p))
def dfs(s):
    v=[0]*(n+1)
    q=[(0,s)]
    v[s]=1
    while q:
        w,e=q.pop()
        for w2,e2 in g[e]:
            if not v[e2]:
                q.append((w+w2,e2))
                v[e2]+=w+w2
    return (max(v),v.index(max(v)))
print(0 if n==1 else dfs(dfs(1)[1])[0])