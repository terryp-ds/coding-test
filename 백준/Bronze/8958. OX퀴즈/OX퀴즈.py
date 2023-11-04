import sys
input=sys.stdin.readline
for _ in range(int(input())): print(sum([(len(i)**2+len(i))//2 for i in input().strip().split('X')]))
