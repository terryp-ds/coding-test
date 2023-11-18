import sys
input=sys.stdin.readline
n=int(input())
a=[[*map(int,input().split())] for _ in range(n)]
d=[[] for _ in range(n)]
d[0]=a[0]
if n>1:d[1]=[a[0][0]+a[1][0],a[0][0]+a[1][1]]
for i in range(2,n): d[i]=[d[i-1][0]+a[i][0]]+[max(d[i-1][j-1],d[i-1][j])+a[i][j] for j in range(1,i)]+[d[i-1][-1]+a[i][-1]]
print(max(d[n-1]))