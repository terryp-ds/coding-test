import sys

input = sys.stdin.readline

n,m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
visited = [0]*n

for v1,v2 in edges:
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

cnt = 0

for i in range(n):
    stack = [i]

    if not visited[i]:
        cnt += 1

        while stack:
            cur = stack.pop()

            if not visited[cur]:
                visited[cur] = 1

                for nex in graph[cur]:
                    if not visited[nex]:
                        stack.append(nex)


print(cnt)