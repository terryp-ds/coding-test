import heapq
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int, input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))

max_ = 0
visited = [0]*(n+1)
heap = [(0,1)]
weight = 0
cnt = 0

while heap:
    if cnt == n:
        break
    
    w,node = heapq.heappop(heap)

    if not visited[node]:
        visited[node] = 1
        weight += w
        cnt += 1
        max_ = max(max_, w)

        for edge in graph[node]:
            heapq.heappush(heap, edge)

print(weight-max_)
