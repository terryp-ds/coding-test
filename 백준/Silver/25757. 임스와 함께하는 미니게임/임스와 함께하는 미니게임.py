import sys
input=sys.stdin.readline
n,m=input().split()
s=set([input() for _ in range(int(n))])
print(len(s)//('YFO'.find(m)+1))