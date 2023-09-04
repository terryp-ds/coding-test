import sys
input = sys.stdin.readline

n,m = map(int, input().split())
r,c,d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
ans = 0

while 1:
    if not a[r][c]:
        a[r][c] = -1
        ans += 1

    f = 0

    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]

        if 0 <= ny < n and 0 <= nx < m and not a[ny][nx]:
            f = 1
            break

    if f:
        while 1:
            d = (d-1) % 4
            ny = r + dy[d]
            nx = c + dx[d]

            if 0 <= ny < n and 0 <= nx < m and not a[ny][nx]:
                break

    else:
        ny = r + dy[d-2]
        nx = c + dx[d-2]

        if not 0 <= ny < n or not 0 <= nx < m or a[ny][nx] == 1:
            break

    r,c = ny,nx

print(ans)