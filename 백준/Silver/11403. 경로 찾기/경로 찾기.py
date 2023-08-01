import heapq
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

graph = [[] for _ in range(n)]

for i, row in enumerate(matrix):
    for j in range(n):
        if row[j]:
            graph[i].append(j)

matrix = []

for i in range(n):
    visited = [0]*n

    stack = []
    stack.extend(graph[i])

    while stack:
        cur = stack.pop()

        if not visited[cur]:
            visited[cur] = 1

            for nex in graph[cur]:
                if not visited[nex]:
                    stack.append(nex)

    matrix.append(visited)
        
    
for row in matrix:
    print(' '.join([str(i) for i in row]))
