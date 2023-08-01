import heapq

n,k = map(int, input().split())
visited = [100000]*200001
visited[n] = 0
heap = [(0, n)]

while heap:
    time, node = heapq.heappop(heap)

    if node == k:
        break

    if node > 0 and time+1 < visited[node-1]:
        visited[node-1] = time+1
        heapq.heappush(heap, (time+1, node-1))

    if node < k and time+1 < visited[node+1]:
        visited[node+1] = time+1
        heapq.heappush(heap, (time+1, node+1))

    if 0 < node < k and time < visited[node*2]:
        visited[node*2] = time
        heapq.heappush(heap, (time, node*2))
    
print(visited[k])
