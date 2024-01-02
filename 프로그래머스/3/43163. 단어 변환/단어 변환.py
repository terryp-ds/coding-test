from collections import deque

def solution(s, t, w):
    w+=[s]
    g={i:[] for i in w}
    v={i:0 for i in w+[t]}
    n,m=len(w),len(s)
    for i in range(n):
        for j in range(i,n):
            if sum([x==y for x,y, in zip(w[i], w[j])])==m-1:
                g[w[i]]+=[w[j]]
                g[w[j]]+=[w[i]]
    q=deque([s])
    v[s] = 1
    
    while q:
        c=q.popleft()
        if c==t:return v[t]-1
        for x in g[c]:
            if not v[x]:
                q+=[x]
                v[x]=v[c]+1
    return 0