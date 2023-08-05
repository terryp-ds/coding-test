import heapq
import sys
input = sys.stdin.readline

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1].append((w,v2))

min_time = [0]*(n+1)

for i in range(1,n+1):
    obj = [i,x]

    for j in range(2):
        visited = [10**6]*(n+1)
        heap = [(0, obj[j])]
        visited[obj[j]] = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node == obj[1-j]:
                min_time[i] += time
                break

            for time2, next_node in graph[node]:
                alt = time + time2

                if alt < visited[next_node]:
                    heapq.heappush(heap, (alt, next_node))
                    visited[next_node] = alt

print(max(min_time))
