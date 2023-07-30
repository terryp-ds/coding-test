import sys

input = sys.stdin.readline
n = int(input())
arr = [1,1,1,2,2]
c = 5
for _ in range(n):
    k = int(input())

    while c < k:
        arr.append(arr[-1]+arr[-5])
        c += 1

    print(arr[k-1])
