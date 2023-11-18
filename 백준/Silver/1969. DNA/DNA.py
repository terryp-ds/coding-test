from collections import Counter
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[input().strip() for _ in range(n)]
t=[[r[i] for r in a] for i in range(m)]
c=[sorted(sorted(Counter(r).items()), key=lambda x: x[1], reverse=True) for r in t]
print(*[x[0][0] for x in c],sep='')
print(sum([n-x[0][1] for x in c]))