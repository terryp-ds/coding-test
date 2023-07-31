from collections import deque

n,k = map(int, input().split())
visited = [0]*200000
level = [0]*200000
queue = deque([n])

while queue:
    cur = queue.popleft()

    if cur == k:
        break

    visited[cur] = 1

    if cur > 0 and not visited[cur-1]:
        queue.append(cur-1)
        if not level[cur-1]:
            level[cur-1] = level[cur]+1

    if cur < 199999 and not visited[cur+1]:
        queue.append(cur+1)
        if not level[cur+1]:
            level[cur+1] = level[cur]+1

    if cur < k:
        queue.append(cur*2)
        if not level[cur*2]:
            level[cur*2] = level[cur]+1

print(level[k])
