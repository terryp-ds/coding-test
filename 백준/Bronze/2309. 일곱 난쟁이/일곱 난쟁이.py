from itertools import combinations
a=[int(input()) for _ in range(9)]
for c in combinations(a,7):
 if sum(c)==100:
  print(*sorted(c),sep='\n')
  break