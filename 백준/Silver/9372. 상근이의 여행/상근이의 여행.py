import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int, input().split())
    print(n-1)
    for _ in range(m):
        _ = input()
