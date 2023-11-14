import sys
input=sys.stdin.readline
n=int(input())
a=[[*map(int,input().split())] for _ in range(n)]
for i in range(1,n):
    for j in range(3):
        a[i][j]=min(a[i-1][(j+1)%3],a[i-1][(j+2)%3])+a[i][j]
print(min(a[n-1]))