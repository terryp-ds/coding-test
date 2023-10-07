from bisect import *
for _ in range(int(input())):
    n,m=map(int,input().split())
    a,b=[sorted([*map(int,input().split())]) for _ in range(2)]
    print(sum([bisect_left(b,i) for i in a]))
