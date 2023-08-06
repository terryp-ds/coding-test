import heapq
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))

visited = [float('inf')]*(n+1)
start, end = map(int, input().split())

heap = [(0,start)]

while heap:
    cost, node = heapq.heappop(heap)

    if node == end:
        break

    for cost2, node2 in graph[node]:
        c = cost + cost2

        if c < visited[node2]:
            visited[node2] = c
            heapq.heappush(heap, (c, node2))

print(visited[end])
