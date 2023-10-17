from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
v=[0]*(n+1)
g=[[] for _ in range(n+1)]
s,e=map(int,input().split())
for _ in range(int(input())):
    x,y=map(int,input().split())
    g[x]+=[y]
    g[y]+=[x]
q=deque([s])
v[s]=1
while q:
    c=q.popleft()
    if c==e: break
    for x in g[c]:
        if not v[x]:
            q.append(x)
            v[x]=v[c]+1
print(v[e]-1)