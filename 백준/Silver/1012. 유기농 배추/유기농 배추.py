import sys

input = sys.stdin.readline

n_case = int(input())

for i in range(n_case):
    m, n, k = map(int, input().split())
    locs = [list(map(int, list(input().split()))) for _ in range(k)]
    maps = [0]*m*n

    for v in locs:
        maps[v[0]+v[1]*m] = 1

    maps = [maps[m*i:m*(i+1)] for i in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    graph = [[] for _ in range(m*n)]

    for y in range(n):

        for x in range(m):

            v = maps[y][x]

            if v:
                for i in range(4):

                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < m and 0 <= ny < n and maps[ny][nx]:
                        graph[y*m+x].append((y+dy[i])*m+(x+dx[i]))

    visited = [0]*m*n
    group = 0

    for i in range(m*n):

        y,x = i//m, i%m

        if maps[y][x] and not visited[i]:

            stack = [i]
            group += 1

            while stack:

                vertex = stack.pop()

                if not visited[vertex]:

                    visited[vertex] = 1

                    for v in graph[vertex]:
                        if not visited[v]:
                            
                            stack.append(v)


    print(group)
