import heapq
import sys
input = sys.stdin.readline

v,e = map(int, input().split())
visited = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    s,e,w = map(int, input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))

heap = [(0,1)]
weight = 0
cnt = 0

while heap:
    if cnt == v:
        break

    w,node = heapq.heappop(heap)

    if not visited[node]:
        visited[node] = 1
        weight += w
        cnt += 1

        for edge in graph[node]:
            heapq.heappush(heap, edge)

print(weight)
