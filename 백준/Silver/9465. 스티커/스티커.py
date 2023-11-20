import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=[[*map(int,input().split())] for _ in range(2)]
    d=[0]*n
    d[0]=[a[0][0],a[1][0]]
    if n==1: print(max(d[0])); continue
    d[1]=[d[0][1]+a[0][1],d[0][0]+a[1][1]]
    for i in range(2,n): d[i]=[max(d[i-1][1],d[i-2][1])+a[0][i],max(d[i-1][0],d[i-2][0])+a[1][i]]
    print(max(d[-1]))