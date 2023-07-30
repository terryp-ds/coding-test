import sys

input = sys.stdin.readline
n = int(input())
people = sorted(map(int, input().split()))
print(sum([sum(people[:i]) for i in range(1, n+1)]))
