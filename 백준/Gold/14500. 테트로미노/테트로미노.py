import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tetris = {
    (0,3):[[(0,0), (0,1), (0,2), (0,3)]],
    (3,0):[[(0,0), (1,0), (2,0), (3,0)]],
    (1,1):[[(0,0), (0,1), (1,0), (1,1)]],
    (1,2):[
        [(0,0), (0,1), (0,2), (1,0)],
        [(0,0), (0,1), (0,2), (1,2)],
        [(0,0), (1,0), (1,1), (1,2)],
        [(1,0), (1,1), (1,2), (0,2)],
        [(0,1), (0,2), (1,0), (1,1)],
        [(0,0), (0,1), (1,1), (1,2)],
        [(0,0), (0,1), (0,2), (1,1)],
        [(0,1), (1,0), (1,1), (1,2)]
        ],
    (2,1):[
        [(0,0), (1,0), (2,0), (0,1)],
        [(0,0), (1,0), (2,0), (2,1)],
        [(0,0), (0,1), (1,1), (2,1)],
        [(0,1), (1,1), (2,1), (2,0)],
        [(1,0), (2,0), (0,1), (1,1)],
        [(0,0), (1,0), (1,1), (2,1)],
        [(0,0), (1,0), (2,0), (1,1)],
        [(1,0), (0,1), (1,1), (2,1)]
        ]
}

dy = [1,-1,0,0]
dx = [0,0,1,-1]

max_sum = 0


for ly,lx in tetris:
    visited = [[0]*m for _ in range(n)]
    stack = [(0,0)]
    
    while stack:
        node = stack.pop()
        y,x = node

        if not visited[y][x]:
            visited[y][x] = 1

            for shape in tetris[(ly, lx)]:
                arr2 = [(y+dy2, x+dx2) for dy2,dx2 in shape]                
                max_sum = max(sum([arr[y][x] for y,x in arr2]), max_sum) 

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= nx < m-lx and 0 <= ny < n-ly:
                    stack.append((ny, nx))
                    

print(max_sum)  
