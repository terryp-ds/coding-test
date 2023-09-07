from collections import deque

def solution(maps):
    r,c = len(maps),len(maps[0])
    v = [[0]*c for _ in range(r)]
    
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    
    q = deque([(0,0)])
    maps[0][0] = 0
    v[0][0] = 1
    
    
    while q:
        y,x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx]:
                q.append((ny,nx))
                maps[ny][nx] = 0
                v[ny][nx] = v[y][x] + 1
                
    t = v[r-1][c-1]
    return t if t else -1