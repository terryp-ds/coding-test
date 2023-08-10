from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

queue = deque([1])

while queue:
    v = queue.popleft()

    for v2 in graph[v]:
        if not visited[v2]:
            visited[v2] = v
            queue.append(v2)

print(*visited[2:], sep='\n')
