import sys
input=sys.stdin.readline
a=[input().strip() for _ in range(int(input()))]
a=[[r[i] for r in a] for i in range(len(a[0]))]
for r in a:
    if len(set(r))==1: print(r[0],end='')
    else: print('?',end='')