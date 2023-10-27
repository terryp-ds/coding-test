import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(x):
    if p[x]!=x: p[x]=find(p[x])
    return p[x]
def union(a,b):
    a,b=find(a),find(b)
    if a<b: a,b=b,a
    p[a]=b
n,m=int(input()),int(input())
e=sorted([[*map(int,input().split())] for _ in range(m)], key=lambda x: x[2])
p=[i for i in range(n+1)]
d=0
for a,b,w in e:
    if find(a)!=find(b): union(a,b); d+=w
print(d)