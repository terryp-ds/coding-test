import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
graph = [[] for _ in range(n)]
dist = [10**10]*n
dist[start-1] = 0

for v1,v2,w in edges:
    graph[v1-1].append((v2-1, w))

heap = [(0, start-1)]

while heap:
    cost, node = heapq.heappop(heap)

    if node == end-1:
        break

    for v2,w in graph[node]:
        alt = cost + w

        if alt < dist[v2]:
            heapq.heappush(heap, (alt, v2))
            dist[v2] = alt


print(dist[end-1])
