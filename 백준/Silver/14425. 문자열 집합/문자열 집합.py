import sys
input=sys.stdin.readline
n,m = map(int,input().split())
s = set([input().strip() for _ in range(n)])
x = [input().strip() for _ in range(m)]
print(len([i for i in x if i in s]))