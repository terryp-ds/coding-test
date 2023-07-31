from collections import deque

n = int(input())
queue = deque([1])
visited = [0]*(10**6+1)

if n == 1:
    print(0)
    
else:
    while 1:
        cur = queue.popleft()

        if cur == n:
            print(visited[cur]-1)
            break
        
        if not visited[cur]:
            visited[cur] = 1

        for nex in [cur+1, cur*2, cur*3]:
            if nex <= n and not visited[nex]:
                queue.append(nex)
                visited[nex] = visited[cur] + 1
