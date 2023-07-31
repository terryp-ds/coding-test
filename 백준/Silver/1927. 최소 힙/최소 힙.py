import heapq
import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

heap = []

for i in arr:
    if i == 0:
        print(heapq.heappop(heap) if heap else 0)

    else:
        heapq.heappush(heap, i)
