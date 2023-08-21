import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

ans = 0

while len(heap) > 1:
    num = heapq.heappop(heap) + heapq.heappop(heap)
    ans += num
    heapq.heappush(heap, num)
    
print(ans)