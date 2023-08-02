from collections import deque
import sys
input = sys.stdin.readline

n, m= map(int,input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
visited = [0]*n
dim = [0]*n

for v1, v2 in edges:
    graph[v1-1].append(v2-1)
    dim[v2-1] += 1

queue = deque([])
sorted_node = []

while len(sorted_node) < n:
    for v in range(n):
        if not dim[v] and not visited[v]:
            queue.append(v)
            visited[v] = 1

    while queue:
        node = queue.popleft()
        sorted_node.append(node+1)

        for v in graph[node]:
            dim[v] -= 1

print(*sorted_node, sep=' ')
