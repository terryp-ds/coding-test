import sys
input=sys.stdin.readline
n=int(input())
g=[[] for _ in range(n+1)]
v=[0]*(n+1)
for _ in range(int(input())):
    s,e=map(int,input().split())
    g[s]+=[e]
    g[e]+=[s]
q=[1]
v[1]=1
while q:
    c=q.pop()
    for x in g[c]:
        if v[x]: continue
        v[x]=1
        q+=[x]
print(sum(v)-1)