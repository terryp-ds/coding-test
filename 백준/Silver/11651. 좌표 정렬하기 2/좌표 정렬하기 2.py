import sys

arr = [[int(j) for j in sys.stdin.readline().strip().split()] for i in range(int(input()))]
arr = sorted(arr, key=lambda x: (x[1], x[0]))

for i in arr:
    print(f'{i[0]} {i[1]}')
