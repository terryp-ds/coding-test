import sys
input=sys.stdin.readline

def find(x):
    if p[x]!=x: p[x]=find(p[x])
    return p[x]

def union(a,b):
    a,b=find(a),find(b)
    if a>b: a,b=b,a
    p[a]=b

n=int(input())
c=[[*map(int,input().split())]+[i] for i in range(n)]
p=[i for i in range(n)]
e=[]

for i in range(3):
    g=sorted(c,key=lambda x:x[i])
    for j in range(len(g)-1):
        e.append((abs(g[j+1][i]-g[j][i]),g[j][3],g[j+1][3]))

e.sort()
d=0

for l in e:
    w,s,e=l
    if find(s)!=find(e):
        union(s,e)
        d+=w

print(d)