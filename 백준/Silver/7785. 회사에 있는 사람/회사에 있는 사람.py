import sys
input = sys.stdin.readline
d={}
for _ in range(int(input())):
    n,s=input().rstrip().split()
    if s=='enter':
        if n not in d:
            d[n]=0
        d[n]=0
    else:
        del d[n]
print(*sorted(d.keys(),reverse=True),sep='\n')