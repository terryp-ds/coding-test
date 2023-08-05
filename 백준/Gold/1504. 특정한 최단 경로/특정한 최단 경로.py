import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, end, graph):
    heap = [(0, start)]
    visited = [float('inf')]*(n+1)
    visited[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if node == end:
            return visited[end]

        for dist2, node2 in graph[node]:
            d = dist + dist2

            if d < visited[node2]:
                visited[node2] = d
                heapq.heappush(heap, (d, node2))

    return -1

n,e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    v1,v2,w = map(int, input().split())
    graph[v1].append((w,v2))
    graph[v2].append((w,v1))

v1, v2 = map(int, input().split())

r1 = [dijkstra(1,v1,graph), dijkstra(v1,v2,graph), dijkstra(v2,n,graph)]
r2 = [dijkstra(1,v2,graph), dijkstra(v2,v1,graph), dijkstra(v1,n,graph)]

if (-1 in r1) or (-1 in r2):
    print(-1)
else:
    print(min(sum(r1), sum(r2)))
