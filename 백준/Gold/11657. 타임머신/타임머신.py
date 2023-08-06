from collections import deque
import sys
input = sys.stdin.readline


n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
edges = [list(map(int, input().split())) for _ in range(m)]

for s,e,t in edges:
    graph[s].append((t,e))

dist = [float('inf') for _ in range(n+1)]
pred = [None for _ in range(n+1)]
dist[1] = 0

for _ in range(1,n+1):
    for s,e,t in edges:
        if dist[s] + t < dist[e]:
            dist[e] = dist[s] + t
            pred[e] = s

flag = 0

arr = []

for i in range(2,n+1):
    if dist[i] == float('inf'):
        arr.append(-1)
        continue

    for s,e,t in edges:
        if dist[s] + t < dist[e]:
            flag = 1
            break

    arr.append(dist[i])
    
    if flag:
        break

if flag:
    print(-1)

else:
    print(*arr, sep='\n')
