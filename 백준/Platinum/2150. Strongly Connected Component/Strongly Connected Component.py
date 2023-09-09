import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def tarjan(V, E):
    S,scc,c = [],[],[0]
    v,f,G=[0 for _ in range(V+1)],[0 for _ in range(V+1)],[[] for _ in range(V+1)]
    
    for s,e in E:
        G[s].append(e)

    def sc(n):
        c[0]+=1
        v[n]=c[0]
        S.append(n)
        a=v[n]
        for x in G[n]:
            if v[x]==0:
                a=min(a,sc(x))
            elif not f[x]:
                a=min(a,v[x])
        if a==v[n]:
            g=[]
            while 1:
                t=S.pop()
                g.append(t)
                f[t]=1
                if t==n:
                    break
            scc.append(g)
        return a

    for i in range(1,V+1):
        if v[i]==0:
            sc(i)
    return scc

V,E=map(int, input().split())
E=[list(map(int, input().split())) for _ in range(E)]
scc=tarjan(V,E)
print(len(scc))
for g in sorted([sorted(i)+[-1] for i in scc]):
    print(*g)
