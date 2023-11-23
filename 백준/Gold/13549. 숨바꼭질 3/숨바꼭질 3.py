from heapq import *
n,k=map(int,input().split())
v={n:0}
q=[(0,n)]
while q:
    t,c=heappop(q)
    if c==k: break
    if 0<c<k and c*2 not in v:
        v[c*2]=t
        heappush(q,(t,c*2))
    if c>0 and c-1 not in v:
        v[c-1]=t+1
        heappush(q,(t+1,c-1))
    if c<k and c+1 not in v:
        v[c+1]=t+1
        heappush(q,(t+1,c+1))
print(v[k])