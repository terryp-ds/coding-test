import sys
input = sys.stdin.readline

v,e,r = map(int, input().split())
graph = [[] for _ in range(v)]

for _ in range(e):
    a,b=map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [0]*v
stack = [r-1]
count = 1

while stack:
    vertex = stack.pop()

    if not visited[vertex]:
        visited[vertex] += count
        count += 1
        for neighbor in sorted(graph[vertex]):
            if not visited[neighbor]:
                stack.append(neighbor)


print(*visited, sep='\n')
