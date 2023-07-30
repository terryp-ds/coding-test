from collections import deque
import sys

input = sys.stdin.readline

v,e,r = map(int, input().split())

graph = [[] for _ in range(v)]

for _ in range(e):
    a,b=map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [0]*v
queue = deque([r-1])
count = 1

while queue:
    vertex = queue.popleft()
    
    if not visited[vertex]:
        visited[vertex] += count
        count += 1
        for neighbor in sorted(graph[vertex], reverse=True):
            if not visited[neighbor]:
                queue.append(neighbor)


print(*visited, sep='\n')
