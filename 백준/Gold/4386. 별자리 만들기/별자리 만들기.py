import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(float, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
visited = [0]*n

for i in range(n):
    for j in range(i+1,n):
        dist = ((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2)**0.5
        graph[i].append((dist, j))
        graph[j].append((dist, i))

cnt = 0
heap = [(0,1)]
weight = 0

while heap:
    if cnt == n:
        break

    w,node = heapq.heappop(heap)

    if not visited[node]:
        visited[node] = 1
        weight += w
        cnt += 1

    for w2,node2 in graph[node]:
        if not visited[node2]:
            heapq.heappush(heap, (w2,node2))

print(weight)