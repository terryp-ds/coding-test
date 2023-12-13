import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[0]+[*map(int,input().split())]
for i in range(1,n+1): a[i]+=a[i-1]
for _ in range(m): 
 i,j=map(int,input().split())
 print(a[j]-a[i-1])