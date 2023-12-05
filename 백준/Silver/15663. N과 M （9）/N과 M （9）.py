from itertools import *
n,m=map(int,input().split())
for p in sorted(set(permutations(map(int,input().split()),m))):print(*p)