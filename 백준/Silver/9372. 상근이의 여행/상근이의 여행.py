import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int, input().split())
    print(n-1)
    _ = [input() for _ in range(m)]
