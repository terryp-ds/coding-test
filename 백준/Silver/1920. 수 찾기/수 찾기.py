import sys
input=sys.stdin.readline
input()
a=set([*map(int,input().split())])
input()
b=[*map(int,input().split())]
print(*[int(i in a) for i in b],sep='\n')
