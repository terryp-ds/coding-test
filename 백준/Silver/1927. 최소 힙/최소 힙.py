from heapq import *
import sys
input = sys.stdin.readline
q=[]
for _ in range(int(input())):
 n=int(input())
 if n:heappush(q,n)
 else:print(heappop(q) if q else 0)