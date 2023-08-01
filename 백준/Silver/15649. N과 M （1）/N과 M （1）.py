from itertools import permutations
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

perm = [' '.join([str(i) for i in p]) for p in permutations(range(1, n+1), m)]

print(*perm, sep='\n')
