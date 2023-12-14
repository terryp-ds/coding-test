import sys
input=lambda:sys.stdin.readline().strip()
m,n=map(int,input().split())
s=set([input() for _ in range(m)])&set([input() for _ in range(n)])
print(len(s))
print(*sorted(s),sep='\n')