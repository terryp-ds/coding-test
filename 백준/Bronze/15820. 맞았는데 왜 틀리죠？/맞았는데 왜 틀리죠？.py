m,n=map(int,input().split())
f=1
for _ in range(m):
 x,y=map(int,input().split())
 if x!=y:f=0
for _ in range(n):
 x,y=map(int,input().split())
 if x!=y:f*=2
print(['Wrong Answer','Accepted','Why Wrong!!!'][f])
