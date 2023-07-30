import sys

input = sys.stdin.readline
m,n = map(int, input().split())
pw_dict = {}

for _ in range(m):
    k,v = input().split()
    pw_dict[k] = v

for _ in range(n):
    print(pw_dict[input().rstrip()])
