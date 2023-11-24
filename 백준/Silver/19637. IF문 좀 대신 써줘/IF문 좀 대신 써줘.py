from bisect import *
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[[*input().split()] for _ in range(n)]
a,p=[i[0] for i in a],[int(i[1]) for i in a]
for _ in range(m): print(a[bisect_left(p,int(input()))])