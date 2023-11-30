from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
score = [[0]*n for _ in range(n)]
edges = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n)]

for v1,v2 in edges:
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

for i in range(n):
    visited = [0]*n
    queue = deque([i])
    c = 0

    while queue:
        cur = queue.popleft()

        if not visited[cur]:
            visited[cur] = 1
            c = score[i][cur]

            for nex in graph[cur]:
                if not visited[nex]:
                    queue.append(nex)

                    if not score[i][nex]:
                        score[i][nex] = c+1

print(sorted(zip(range(1,n+1), map(sum, score)), key=lambda x:(x[1], x[0]))[0][0])
