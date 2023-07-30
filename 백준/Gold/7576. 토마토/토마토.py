import sys

input = sys.stdin.readline

m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
stack = [[y,x] for x in range(m) for y in range(n) if graph[y][x] == 1]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
day = 0

while stack:
    new_stack = []

    for y,x in stack:

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not graph[ny][nx]:
                    new_stack.append([ny, nx])
                    graph[ny][nx] = 1

    stack = new_stack

    if stack:
        day += 1

print(day if not sum(map(lambda x: x.count(0), graph)) else -1)
