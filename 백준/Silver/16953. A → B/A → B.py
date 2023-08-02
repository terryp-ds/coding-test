from collections import deque

a,b = map(int, input().split())

visited = {}

queue = deque([a])
visited[a] = 1

while queue:
    node = queue.popleft()

    for next_node in [node*2, node*10+1]:
            
            if next_node <= b and next_node not in visited:
                queue.append(next_node)
                visited[next_node] = visited[node]+1

print(visited[b] if b in visited else -1)
