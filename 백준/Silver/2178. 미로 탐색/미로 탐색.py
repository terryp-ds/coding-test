from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]
graph = [[] for _ in range(n*m)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for y in range(n):
    for x in range(m):
        if maps[y][x]:
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0 <= nx < m and 0 <= ny < n and maps[ny][nx]:
                    graph[x+y*m].append(nx+ny*m)

visited = [0]*n*m
route = []
queue = deque([0])
pred = [[] for _ in range(n*m)]

while queue:
    cur = queue.popleft()

    if cur == n*m-1:
        print(len(pred[-1])+1)
        break

    if not visited[cur]:
        visited[cur] = 1
        route.append(cur)

        for nex in graph[cur]:
            if not visited[nex]:
                queue.append(nex)
                if not pred[nex]:
                    pred[nex].extend(pred[cur]+[cur])
