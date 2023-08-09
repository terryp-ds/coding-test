import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if arr[i] > arr[j] and lis[i] < lis[j]+1:
            lis[i] = lis[j] + 1

print(max(lis))
