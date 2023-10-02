from collections import deque
import sys
input=sys.stdin.readline

def init(n,e,r):
    g=[[] for _ in range(n+1)]
    for a,b in e: 
        g[a]+=[b]
        g[b]+=[a]

    v,d,t=[[0 for _ in range(n+1)] for _ in range(3)]
    v[r]=1
    q=deque([r])

    while len(q):
        c=q.popleft()
        for x in g[c]:
            if not v[x]:
                d[x]=d[c]+1
                v[x]=1
                t[x]=c
                q.append(x)
    return t,d

def sparse(n,t):
    s=[[0 for _ in range(18)] for _ in range(n+1)]
    for i in range(1,n+1): s[i][0]=t[i]

    b=1
    while (1<<b)<n:
        for i in range(1,n+1):
            if s[i][b-1]!=0:
                s[i][b]=s[s[i][b-1]][b-1]
        b+=1
    return s

def lca(t,d,s,u,v):
    if d[u]<d[v]: u,v=v,u
    b=d[u].bit_length()

    for i in range(b,-1,-1): 
        if d[u]-(1<<i)>=d[v]: u=s[u][i]

    if u==v: return u
    for i in range(b,-1,-1):
        if s[u][i]!=0 and s[u][i]!=s[v][i]: u,v=s[u][i],s[v][i]
    return t[u]

n=int(input())
e=[[*map(int,input().split())] for _ in range(n-1)]
t,d=init(n,e,1)
s=sparse(n,t)

for _ in range(int(input())):
    u,v=map(int,input().split())
    print(lca(t,d,s,u,v))