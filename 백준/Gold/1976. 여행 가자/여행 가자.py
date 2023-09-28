import sys
input=sys.stdin.readline

def find(x):
    if p[x]!=x: p[x]=find(p[x])
    return p[x]

def union(a,b):
    a,b=find(a),find(b)
    if a<b: p[b]=a
    elif a>b: p[a]=b

n,m=int(input()),int(input())
p=[i for i in range(n)]
for i in range(n):
    a=[*map(int,input().split())]
    for j in range(n):
        if a[j]: union(i,j)

a=[*map(int,input().split())]
p=[p[i-1] for i in a]
print('YES' if sum(p)/len(p)==p[0] else 'NO')