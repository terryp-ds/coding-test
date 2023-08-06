from collections import deque

n,k = map(int, input().split())

queue = deque([n])
visited = [100000]*200000
visited[n] = 0
cnt = 0
min_time = 100001

if k < n:
    print(n-k)
    print(1)

else:
    while queue:
        node = queue.popleft()
        time = visited[node]

        if node == k:
            if time <= min_time:
                min_time = time
                cnt += 1
            continue

        if visited[node] > min_time:
            break

        for node2 in [node-1, node+1, node*2]:
            if 0 <= node2 < k*2 and time < visited[node2]:
                queue.append(node2)
                visited[node2] = time + 1

    print(min_time)
    print(cnt)
