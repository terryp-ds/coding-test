from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

queue = deque([(0,0,0)])
visited[0][0][0] = 1

while queue:
    y,x,b = queue.popleft()

    if y== n-1 and x == m-1:
        print(visited[y][x][b])
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx][b] and arr[ny][nx] == 0:
                queue.append((ny, nx, b))
                visited[ny][nx][b] = visited[y][x][b] + 1

            if not b and arr[ny][nx] == 1 and not visited[ny][nx][1]:
                queue.append((ny, nx, 1))
                visited[ny][nx][1] = visited[y][x][b] + 1
    
if not (y == n-1 and x == m-1):
    print(-1)
