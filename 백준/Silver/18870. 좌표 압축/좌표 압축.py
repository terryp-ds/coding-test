import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(set(arr))

d = {}


for i in range(len(arr2)):
    d[arr2[i]] = i

print(*[d[i] for i in arr], sep=' ')
