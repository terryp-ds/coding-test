import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
dist = [[10**8+1 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    dist[i][i] = 0

for v1, v2, w in arr:
    dist[v1][v2] = min(w, dist[v1][v2])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
for i in range(1,n+1):
    row = dist[i][1:]

    for j in range(n):
        if row[j] == 10**8+1:
            row[j] = 0

    print(*row, sep=' ')
