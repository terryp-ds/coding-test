from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = sum(map(sum, arr))
time = 0
dy = [1,-1,0,0]
dx = [0,0,1,-1]

while cnt:

    queue = deque([(0,0)])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 1 and not visited[ny][nx]:
                queue.append((ny,nx))
                visited[ny][nx] = 1

    for y in range(n):
        for x in range(m):
            if arr[y][x] == 0 and not visited[y][x]:
                arr[y][x] = -1

            elif arr[y][x] == -1 and visited[y][x]:
                arr[y][x] = 0

    to_del = []

    for y in range(n):
        for x in range(m):
            if arr[y][x] != 1:
                continue

            adj = 0

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if arr[ny][nx] == 0:
                    adj += 1

            if adj >= 2:
                to_del.append((y,x))

    for y,x in to_del:
        arr[y][x] = 0
        cnt -= 1

    time += 1

print(time)
