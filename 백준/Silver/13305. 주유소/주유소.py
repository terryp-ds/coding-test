n=int(input())
d,c=[[*map(int,input().split())] for _ in range(2)]
v=[0]*(n-1)
m=c[0]
x=0
for i in range(n-1):
 if m>c[i]:
  m=c[i]
  x=i
 v[x]+=d[i]
print(sum([x*y for x,y in zip(c,v)]))