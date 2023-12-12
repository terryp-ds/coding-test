import sys
input=sys.stdin.readline
m,n=map(int,input().split())
s=set([input().strip() for _ in range(m)])&set([input().strip() for _ in range(n)])
print(len(s))
print(*sorted(s),sep='\n')