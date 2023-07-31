import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())

    if not x:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))

    else:
        heapq.heappush(heap, -x)
