from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    y1, x1 = map(int, input().split())
    y2, x2 = map(int, input().split())

    queue = deque([[y1, x1]])

    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    visited = [[0]*n for _ in range(n)]
    visited[y1][x1] = 1

    while queue:
        cur = queue.popleft()
        y,x = cur

        if y == y2 and x == x2:
            break

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny <n and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x]+1

    print(visited[y2][x2]-1)
