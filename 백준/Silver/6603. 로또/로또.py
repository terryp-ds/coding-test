from itertools import combinations
f=1
while 1:
 k,*s=map(int,input().split())
 if not k:break
 if f:f=0
 else:print()
 for c in combinations(s,6):print(*c)