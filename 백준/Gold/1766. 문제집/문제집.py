import sys
input = sys.stdin.readline

n, m = map(int,input().split())
vertice = [i for i in range(n)]
edges = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
graph2 = [[] for _ in range(n)]
visited = [0]*n
dim = [0]*n

for v1, v2 in edges:
    graph2[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)
    dim[v2-1] += 1

sorted_node = []

while len(sorted_node) < n:
    for i in vertice:
        if not dim[i] and not visited[i]:
            node = i
            break

    if not visited[node]:
        visited[node] = 1
        sorted_node.append(node+1)
        vertice.remove(node)

        for v in graph2[node]:
            dim[v] -= 1

    
print(*sorted_node, sep=' ')
