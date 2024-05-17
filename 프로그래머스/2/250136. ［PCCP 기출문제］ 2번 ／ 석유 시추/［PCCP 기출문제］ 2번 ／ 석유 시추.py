def solution(land):
    m,n = len(land[0]),len(land)
    dy,dx = [1,-1,0,0],[0,0,1,-1]
    answer = 0
    
    ans_dict = {k:0 for k in range(m)}
    visited = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not land[i][j] or visited[i][j]: continue
            visited[i][j] = 1
            stack = [(i,j)]
            cnt = 1
            cols = [j]
            while stack:
                y,x = stack.pop()
                for k in range(4):
                    ny,nx = y+dy[k], x+dx[k]
                    if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and land[ny][nx]:
                        stack.append((ny,nx))
                        visited[ny][nx] = 1
                        cnt += 1
                        cols.append(nx)
            
            for col in set(cols): ans_dict[col] += cnt
    
    return max(ans_dict.values())