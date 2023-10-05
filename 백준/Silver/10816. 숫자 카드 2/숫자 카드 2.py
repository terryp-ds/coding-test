from collections import Counter
import sys
input=sys.stdin.readline

input()
a=sorted([*map(int,input().split())])
input()
b=[*map(int,input().split())]
c=Counter(a)
print(*[c[i] for i in b])
