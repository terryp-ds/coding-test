import sys
input = sys.stdin.readline

arr = [[0]*15 for _ in range(15)]
arr[0] = [i for i in range(15)]

for i in range(15):
    arr[i][1] = 1

for i in range(1, 15):
    for j in range(2, 15):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for _ in range(int(input())):
    n,k = [int(input()) for _ in range(2)]
    print(arr[n][k])
