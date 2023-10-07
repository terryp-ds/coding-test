from bisect import *
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n,m=map(int,input().split())
    a,b=[sorted([*map(int,input().split())]) for _ in range(2)]
    c=0
    for i in a: c+=bisect_left(b,i)
    print(c)