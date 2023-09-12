import sys
input=sys.stdin.readline

n,m=int(input()),int(input())
g=[[] for _ in range(n+1)]
e=[list(map(int, input().split())) for _ in range(m)]

for u,v in e:
    g[u].append(v)
    g[v].append(u)

v=[0]*(n+1)
s=[1]

while s:
    c=s.pop()
    if not v[c]:
        v[c]=1
        for x in g[c]:
            if not v[x]:
                s.append(x)

print(sum(v)-1)