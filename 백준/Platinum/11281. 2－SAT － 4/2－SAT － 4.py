import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def tarjan(V,E):
    g=[[] for _ in range(2*V+1)]
    for s,e in E:
        g[-s]+=[e]
        g[-e]+=[s]
    q,s,c=[],[],[0]
    v,f=[[0 for _ in range(2*V+1)] for _ in range(2)]
    def dfs(n):
        c[0]+=1
        v[n]=c[0]
        q.append(n)
        a=v[n]
        for x in g[n]:
            if v[x]==0: a=min(a,dfs(x))
            elif not f[x]: a=min(a,v[x])
        if a==v[n]:
            p=[]
            while 1:
                t=q.pop()
                p.append(t)
                f[t]=1
                if t==n: break
            s.append(p)
        return a
    for i in range(1,2*V+1):
        if not v[i]: dfs(i)
    return s
V,E=map(int,input().split())
E=[list(map(int,input().split())) for _ in range(E)]
scc=tarjan(V,E)
d=[0]*(2*V+1)
for i in range(len(scc)):
    for n in scc[i]: d[n]=i
f=1
s=[0]*V
for i in range(1,V+1):
    if d[i]==d[-i]: f=0; break
    if d[i]<d[-i]: s[i-1]=1
print(f)
if f: print(*s)