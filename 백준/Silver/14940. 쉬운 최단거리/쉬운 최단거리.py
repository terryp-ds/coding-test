from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
level = [[0]*m for _ in range(n)]
start = None

for y in range(n):
    for x in range(m):
        if maps[y][x] == 2:
            start = [y,x]


queue = deque([start])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while queue:
    y,x = queue.popleft()
    
    if not visited[y][x]:
        visited[y][x] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if maps[ny][nx] and not level[ny][nx]:
                    queue.append([ny, nx])
                    level[ny][nx] = level[y][x] + 1

for y in range(n):
    for x in range(m):
        if level[y][x] == 0 and maps[y][x] == 1:
            level[y][x] = -1
        

for row in level:
    print(*row, sep=' ')
