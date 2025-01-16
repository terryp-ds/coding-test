import sys
input=sys.stdin.readline
for x in sorted([float(input()) for _ in range(int(input()))])[:7]:print('{:.3f}'.format(x))