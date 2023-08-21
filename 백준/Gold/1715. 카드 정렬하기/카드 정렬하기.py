import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)

ans = 0

while len(heap) > 1:
    num = heapq.heappop(heap) + heapq.heappop(heap)
    ans += num
    heapq.heappush(heap, num)
    
print(ans)
