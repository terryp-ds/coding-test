import sys

input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr = sorted(arr, key=lambda x: (x[1], x[0]))
reserve = [arr[0]]

for i in arr[1:]:
    if i[0] >= reserve[-1][-1]:
        reserve.append(i)

print(len(reserve))
