import sys

input = sys.stdin.readline

n,m = map(int, input().split())
maps = [input().rstrip() for _ in range(n)]
start = None

for i in range(n):
    if maps[i].find('I') != -1:
        start = [i, maps[i].find('I')]
        break

dx = [1,-1,0,0]
dy = [0,0,1,-1]

stack = [start]
visited = [[0]*m for _ in range(n)]
cnt = 0

while stack:
    cur = stack.pop()
    y,x = cur

    if not visited[y][x]:
        visited[y][x] = 1

        if maps[y][x] == 'P':
            cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    stack.append([ny, nx])


print(cnt if cnt else 'TT')
