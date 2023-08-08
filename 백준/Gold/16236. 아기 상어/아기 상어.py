from collections import deque
import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[400]*n for _ in range(n)]
d = {i:[] for i in range(10)}
lv,exp = 2,0

for i in range(n):
    for j in range(n):
        d[arr[i][j]].append((i,j))

dy = [-1,0,0,1]
dx = [0,-1,1,0]

y,x = d[9][0]
arr[y][x] = 0
visited[y][x] = 0

cnt = len(d[1])
total_time = 0
time = 0

queue = deque([(y,x)])
prey = []

while queue:
    y,x = queue.popleft()
    t = visited[y][x]

    if 0 < time == t:
        y,x = heapq.heappop(prey)
        d[arr[y][x]].remove((y,x))
        arr[y][x] = 0
        cnt -= 1
        exp += 1

        if lv == exp < 8:
            lv += 1
            exp = 0
            cnt += len(d[lv-1])

        total_time += time
        time = 0
        visited = [[400]*n for _ in range(n)]
        visited[y][x] = 0
        queue = deque([(y,x)])
        prey = []
        continue

    if not cnt:
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            if t < visited[ny][nx]+1 and arr[ny][nx] <= lv:
                if 0 < arr[ny][nx] < lv:
                    time = t+1
                    heapq.heappush(prey, (ny,nx))

                visited[ny][nx] = t+1
                queue.append((ny,nx))

print(total_time)           
