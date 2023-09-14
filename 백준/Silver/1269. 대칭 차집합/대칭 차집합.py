import sys
input=sys.stdin.readline
_=input()
print(len(set([*map(int,input().split())])^set([*map(int,input().split())])))
