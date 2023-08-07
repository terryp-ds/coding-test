from collections import deque
from itertools import combinations

n,m = map(int, (input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
v = [(i,j) for i in range(n) for j in range(m) if arr[i][j] == 2]
z = [(i,j) for i in range(n) for j in range(m) if arr[i][j] == 0]

cz = len(z) - 3

dy = [1,-1,0,0]
dx = [0,0,1,-1]

c = combinations(z, 3)
max_area = 0

for w1,w2,w3 in c:
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    
    for vy,vx in v:
        queue = deque([(vy,vx)])
        
        while queue:
            node = queue.popleft()
            y,x = node

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                    if not arr[ny][nx] and (ny,nx) not in (w1,w2,w3):
                        queue.append((ny,nx))
                        visited[ny][nx] = 1
                        cnt += 1
    
    area = cz - cnt
    
    if area > max_area:
        max_area = area

print(max_area)
