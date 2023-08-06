import heapq
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(int(input())):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))

visited = [float('inf')]*(n+1)
min_route = [0]*(n+1)

s,e = map(int, input().split())

heap = [(0,s,[s])]
visited[s] = 0

while heap:
    cost, node, route = heapq.heappop(heap)

    if node == e:
        break

    for cost2, node2 in graph[node]:
        c = cost + cost2

        if c < visited[node2]:
            visited[node2] = c
            heapq.heappush(heap, (c, node2, route+[node2]))
            min_route[node2] = route+[node2]

print(visited[e])
print(len(min_route[e]))
print(*min_route[e])
