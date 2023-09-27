from itertools import combinations
l,c=map(int, input().split())
a=sorted(input().split())
for comb in combinations(a,l):
    if 0<len(set('aeiou')&set(comb))<l-1: print(''.join(comb))