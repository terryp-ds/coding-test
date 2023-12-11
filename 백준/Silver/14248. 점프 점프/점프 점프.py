n=int(input())
a=[*map(int,input().split())]
s=int(input())
q=[s-1]
v=[0]*n
v[s-1]=1
while q:
 c=q.pop()
 for x in [c-a[c],c+a[c]]:
  if 0<=x<n and not v[x]:
   v[x]=1
   q+=[x]
print(sum(v))