import sys
input=sys.stdin.readline

m=int(input())
a=[0]+[*map(int,input().split())]
d=[[a[i]] for i in range(m+1)]

for i in range(1,19):
    for j in range(1,m+1):
        d[j].append(d[d[j][i-1]][i-1])

for i in range(int(input())):
    n,x=map(int,input().split())
    for j in range(18,-1,-1):
        if n>=1<<j:
            n-=1<<j
            x=d[x][j]
    print(x)