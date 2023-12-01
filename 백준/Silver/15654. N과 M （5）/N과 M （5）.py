from itertools import *
n,m=map(int,input().split())
for p in permutations(sorted([*map(int,input().split())]),m):print(*p)