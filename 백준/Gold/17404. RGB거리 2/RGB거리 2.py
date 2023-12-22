import sys
input=sys.stdin.readline
n=int(input())
a=[[*map(int,input().split())] for _ in range(n)]
m=10**7
for i in range(3):
 d=[[m]*3 for _ in range(n)]
 d[0][i]=a[0][i]
 for j in range(1,n):
  for k in range(3):d[j][k]=a[j][k]+min(d[j-1][(k+1)%3],d[j-1][(k+2)%3])
  for j in range(1,3):m=min(m,d[-1][(i+j)%3])
print(m)