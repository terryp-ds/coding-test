import sys
input=sys.stdin.readline
n,m=map(int,input().split())
p=[input().strip() for _ in range(n)]
d=dict(zip(p,range(1,n+1)))
r=dict(zip(range(1,n+1),p))
for _ in range(m):
    q=input().strip()
    print(d[q] if q.isalpha() else r[int(q)])