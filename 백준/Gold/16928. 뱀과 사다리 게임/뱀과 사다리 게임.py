from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n+m)]
ladder = [i[0] for i in edges[:n]]
snake = [i[0] for i in edges[n:]]
graph = [0]*100
level = [0]*100

for v1, v2 in edges:
    graph[v1-1] = v2-1

for i in range(100):
    if not graph[i]:
        graph[i] = i

queue = deque([0])
level[0] = 1

while queue:
    cur = queue.popleft()
    if level[-1]:
        break
    
    next_nodes = [graph[min(cur+i, 99)] for i in range(1,7)]
    for nex in next_nodes:
        if not level[nex]:
            level[nex] = level[cur]+1
            queue.append(nex)
     
    
print(level[-1]-1)
