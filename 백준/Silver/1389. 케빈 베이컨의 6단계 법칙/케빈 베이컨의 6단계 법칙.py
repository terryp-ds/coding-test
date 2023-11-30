n,m=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(m)]
v=[[101 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1): v[i][i]=0
for s,e in a: v[s][e]=v[e][s]=1
for k in range(1,n+1):
   for i in range(1,n+1):
       for j in range(1,n+1):
            v[i][j]=min(v[i][j],v[i][k]+v[k][j])
v=[sum(r) for r in v]
print(v.index(min(v)))