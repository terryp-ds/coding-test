import heapq
import sys
input = sys.stdin.readline

heap = []

for i in range(int(input())):
    n = int(input())

    if not n:
        if not heap:
            print(0)

        else:
            p = heapq.heappop(heap)
            print(p[-1])

    else:
        heapq.heappush(heap, (abs(n), n))
