from collections import deque
def solution(n, edge):
    g = [[] for _ in range(n+1)]
    for s,e in edge:
        g[s]+=[e]
        g[e]+=[s]
    q = deque([1])
    v = [0]*(n+1)
    v[1]=1
    while q:
        c = q.popleft()
        for x in g[c]:
            if v[x]: continue
            q+=[x]
            v[x]+=v[c]+1
    return v.count(max(v))