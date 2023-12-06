from itertools import *
n,m=map(int,input().split())
for c in combinations_with_replacement(sorted(set(map(int,input().split()))),m):print(*c)