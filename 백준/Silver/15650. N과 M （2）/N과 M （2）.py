from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

comb = [' '.join([str(i) for i in p]) for p in combinations(range(1, n+1), m)]

print(*comb, sep='\n')
