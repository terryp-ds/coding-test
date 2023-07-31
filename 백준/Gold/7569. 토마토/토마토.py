import sys

input = sys.stdin.readline

m,n,h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n*h)]
graph = [graph[n*i:n*(i+1)] for i in range(h)]
stack = [[z,y,x] for x in range(m) for y in range(n) for z in range(h) if graph[z][y][x] == 1]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
day = 0

while stack:
    new_stack = []

    for z,y,x in stack:

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if not graph[nz][ny][nx]:
                    new_stack.append([nz, ny, nx])
                    graph[nz][ny][nx] = 1

    stack = new_stack

    if stack:
        day += 1

flag = 1

for k in range(h):
    for j in range(n):
        for i in range(m):
            if not graph[k][j][i]:
                flag = 0
                break

print(day if flag else -1)
