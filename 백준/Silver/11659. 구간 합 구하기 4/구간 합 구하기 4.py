import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
idx = [list(map(int, input().split())) for _ in range(m)]
csum = [0]

for i in range(n):
    csum.append(csum[-1]+arr[i])


print(*[csum[j]-csum[i-1] for i,j in idx], sep='\n')
