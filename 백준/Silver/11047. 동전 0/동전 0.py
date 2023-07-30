import sys

input = sys.stdin.readline
n, target = map(int, input().split())
coins = [int(input()) for _ in range(n)][::-1]
cnt = 0

for coin in coins:
    cnt += target // coin
    target = target % coin

print(cnt)
