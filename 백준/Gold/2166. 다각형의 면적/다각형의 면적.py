import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = arr + [arr[0]]
a = sum([arr[i+1][0]*arr[i][1] for i in range(n)])
b = sum([arr[i+1][1]*arr[i][0] for i in range(n)])

print(abs(a-b)/2)