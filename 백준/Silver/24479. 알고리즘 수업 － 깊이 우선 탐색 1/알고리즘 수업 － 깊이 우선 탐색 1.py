import sys
input=sys.stdin.readline

n,m,r=map(int, input().split())
g=[[] for _ in range(n+1)]

for _ in range(m):
    s,e=map(int, input().split())
    g[s].append(e)
    g[e].append(s)

v=[0]*(n+1)
s=[r]
o=1

while s:
    c=s.pop()
    if not v[c]:
        v[c]=o
        o+=1
        for x in sorted(g[c], reverse=True):
            if not v[x]:
                s.append(x)

print(*v[1:], sep='\n')