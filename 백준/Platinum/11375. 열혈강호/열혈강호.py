import sys
input=sys.stdin.readline
def match(i):
    if v[i]: return 0
    v[i]=1
    for x in g[i]:
        if not s[x] or match(s[x]):
            s[x]=i
            return 1
    return 0
n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
for i in range(n):
    e=[*map(int,input().split())][1:]
    g[i+1]+=e
s=[0]*(m+1)
for i in range(1,n+1):
    v=[0]*(n+1)
    match(i)
a=0
for i in range(1,m+1):
    if s[i]: a+=1
print(a)