import sys

input = sys.stdin.readline

graph = [[] for _ in range(int(input()))]
edges = [list(map(int, input().split())) for _ in range(int(input()))]

for v1, v2 in edges:
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

stack = [0]
visited = [0]*len(graph)
c = -1

while stack:
    cur = stack.pop()

    if not visited[cur]:
        c += 1
        visited[cur] = 1

        for nex in graph[cur]:
            if not visited[nex]:
                stack.append(nex)

print(c)
