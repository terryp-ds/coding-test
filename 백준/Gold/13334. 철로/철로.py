from heapq import *
import sys
input=sys.stdin.readline
p,q=[],[]
for _ in range(int(input())):
    s,e=map(int,input().split())
    if s>e: s,e=e,s
    heappush(q,(e,s))
d=int(input())
c,m=0,0
while q:
    e,s=heappop(q)
    if e-s<=d:
        heappush(p,(s,e))
        c+=1
    while p:
        u,v=heappop(p)
        if e-u>d: c-=1
        else:
            heappush(p,(u,v))
            break
    m=max(m,c)
print(m)