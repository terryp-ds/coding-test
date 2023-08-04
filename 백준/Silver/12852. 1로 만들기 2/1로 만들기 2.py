from collections import deque

n = int(input())

queue = deque([[n]])
visited = [10**6]*(n+1)
visited[n] = 0
cnt = 0

while queue:
    nodes = queue.popleft()
    node = nodes[-1]
    v = visited[node]
    
    if node == 1:
        break
    
    if not node % 3 and v+1 < visited[node//3]:
        queue.append(nodes+[node//3])
        visited[node//3] = v+1

    if not node % 2 and v+1 < visited[node//2]:
        queue.append(nodes+[node//2])
        visited[node//2] = v+1

    if v+1 < visited[node-1]:
        queue.append(nodes+[node-1])
        visited[node-1] = v+1
    
print(visited[1])
print(*nodes, sep=' ')
