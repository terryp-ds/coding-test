import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(m)]

csum = [[0]*(n+1)] + [[0]+[sum(arr[i][:j+1]) for j in range(n)] for i in range(n)]

for i in range(1,n+1):
    csum[i] = [i+j for i,j in zip(csum[i-1], csum[i])]

for x1,y1,x2,y2 in arr2:
    print(csum[x2][y2]-csum[x1-1][y2]-csum[x2][y1-1]+csum[x1-1][y1-1])
