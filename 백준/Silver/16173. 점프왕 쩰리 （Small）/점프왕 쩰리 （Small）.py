n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*n for _ in range(n)]
dy,dx = [1,0],[0,1]
s = [(0,0)]
v[0][0] = 1
f = 0

while s:
    y,x = s.pop()
    m = a[y][x]
    
    if m == -1:
        f = 1
        break
    
    for i in range(2):
        ny = y + dy[i]*m
        nx = x + dx[i]*m
        
        if 0 <= ny < n and 0 <= nx < n and not v[ny][nx]:
            s.append((ny,nx))
            v[ny][nx] = 1

print('HaruHaru' if f else 'Hing')