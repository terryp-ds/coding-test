import sys

input = sys.stdin.readline
n = int(input())
graph = [input().rstrip() for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = [0]*2
blind = {'R':0, 'G':0, 'B':1}

for t in range(2):
    visited = [0]*n*n
    
    for i in range(n*n):
        stack = [i]
        
        if not visited[i]:
            cnt[t] += 1
        
            while stack:
                cur = stack.pop()
            
                if not visited[cur]:
                    visited[cur] = 1
                    y,x = cur//n, cur%n
                    
                    for j in range(4):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx+ny*n]:
                            if t:
                                if blind[graph[ny][nx]] == blind[graph[y][x]]:
                                    stack.append(nx+ny*n)

                            else:
                                if graph[ny][nx] == graph[y][x]:
                                    stack.append(nx+ny*n)


print(*cnt, sep=' ')
