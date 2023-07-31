import heapq
import sys

input = sys.stdin.readline

v,e = map(int, input().split())
s = int(input()) - 1
edges = [list(map(int, input().split())) for _ in range(e)]
graph = [[] for _ in range(v)]
dist = [10**7]*v
dist[s] = 0

for v1,v2,w in edges:
    graph[v1-1].append((v2-1, w))

heap = [(0,s)]

while heap:
    time, node = heapq.heappop(heap)

    if not dist[node]:
        dist[node] = time

    for v2,w in graph[node]:
        alt = time + w

        if alt < dist[v2]:
            heapq.heappush(heap, (alt, v2))
            dist[v2] = alt

for i in range(v):
    if dist[i] == 10**7:
        dist[i] = 'INF'

print(*dist, sep='\n')
