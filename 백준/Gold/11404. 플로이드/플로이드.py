import sys
input=sys.stdin.readline
n,m=int(input()),int(input())
a=[[*map(int,input().split())] for _ in range(m)]
v=[[10**8 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1): v[i][i]=0
for s,e,w in a: v[s][e]=min(w,v[s][e])
for k in range(1,n+1):
   for i in range(1,n+1):
       for j in range(1,n+1):
            v[i][j]=min(v[i][j],v[i][k]+v[k][j])
for i in range(1,n+1): v[i][i]=0
for r in v[1:]: print(*[[0,i][i<10**8] for i in r[1:]])