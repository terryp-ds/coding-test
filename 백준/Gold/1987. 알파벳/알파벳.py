import sys
input = sys.stdin.readline

def dfs(x,y,cnt):
    global max_len

    max_len = max(max_len, cnt)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and not visited[arr[ny][nx]]:
            visited[arr[ny][nx]] = 1
            dfs(nx,ny,cnt+1)
            visited[arr[ny][nx]] = 0

r,c = map(int, input().split())
arr = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]
visited = [0]*26

dy = [1,-1,0,0]
dx = [0,0,1,-1]

visited[arr[0][0]] = 1
max_len = 1
dfs(0,0,max_len)

print(max_len)
