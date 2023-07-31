from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n)]
    
    for v1,v2 in edge:
        graph[v1-1].append(v2-1)
        graph[v2-1].append(v1-1)
    
    queue = deque([0])
    visited = [0]*n
    level = [1]+[0]*(n-1)
    
    while queue:
        cur = queue.popleft()
        
        if not visited[cur]:
            visited[cur] = 1
            
            for nex in graph[cur]:
                if not visited[nex]:
                    queue.append(nex)
                    
                    if not level[nex]:
                        level[nex] = level[cur] + 1
                    
            
    return level.count(max(level))