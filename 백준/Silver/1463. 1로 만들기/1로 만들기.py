n=int(input())
d=[0]*(n+1)
for i in range(2,n+1):
 d[i]=d[i-1]+1
 for k in (2,3):
  if i%k==0:d[i]=min(d[i],d[i//k]+1)
print(d[n])