import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[i for i in range(1,n+1)]
for x in range(m):
    i,j=map(int,input().split())
    a[i-1],a[j-1]=a[j-1],a[i-1]
print(*a)