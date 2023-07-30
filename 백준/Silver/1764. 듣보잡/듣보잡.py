import sys

input = sys.stdin.readline
m,n = map(int, input().split())
sets = set([input().rstrip() for _ in range(m)]).intersection(set([input().rstrip() for _ in range(n)]))
print(len(sets))
print(*sorted(sets), sep='\n')
