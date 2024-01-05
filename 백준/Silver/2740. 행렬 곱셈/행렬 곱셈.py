n,m=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(n)]
m,k=map(int,input().split())
b=[[*map(int,input().split())] for _ in range(m)]
x=[]
for r in a:
 z=[]
 for c in [[r[i] for r in b] for i in range(k)]:
  z+=[sum([i*j for i,j in zip(r,c)])]
 x+=[z]
for r in x:print(*r)