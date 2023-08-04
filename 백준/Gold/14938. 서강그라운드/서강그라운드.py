import heapq
import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())
items = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(r)]
graph = [[] for _ in range(n+1)]

for v1, v2, w in edges:
    graph[v2].append((w, v1))
    graph[v1].append((w, v2))


max_items = 0

for i in range(1, n+1):
    heap = [(0, i)]
    total_items = 0
    dist = [2000]*(n+1)
    visited = [0]*(n+1)
    dist[i] = 0
    
    while heap:
        w, node = heapq.heappop(heap)

        if not visited[node]:
            total_items += items[node-1]
            visited[node] = 1

        for w2,v in graph[node]:
            alt = dist[node] + w2
            
            if alt < dist[v] and alt <= m:
                dist[v] = alt
                heapq.heappush(heap, (w,v))

        max_items = max(max_items, total_items)

print(max_items)
