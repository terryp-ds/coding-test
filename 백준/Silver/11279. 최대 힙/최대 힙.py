from heapq import *
import sys
input=sys.stdin.readline
q=[]
for _ in range(int(input())):
    x=int(input())
    if x: heappush(q,-x)
    else:
        if q:print(-heappop(q))
        else:print(0)