import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
d=[0]*n
d[0]=a[0]
if n==1: print(d[0])
else:
    d[1]=a[0]+a[1]
    for i in range(2,n): d[i] = max(d[i-3]+a[i-1]+a[i], d[i-2]+a[i])
    print(d[n-1])
