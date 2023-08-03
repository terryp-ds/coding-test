import heapq
import sys
input = sys.stdin.readline

def sync(heap):
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)


t = int(input())

for _ in range(t):
    min_heap = []
    max_heap = []
    
    c = 0
    k = int(input())
    visited = [0]*k
    
    for i in range(k):
        c, n = input().rstrip().split()
        n = int(n)

        if c == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = 1

        else:
            if n == 1:
                sync(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
                    
            else:
                sync(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
    
    sync(max_heap)
    sync(min_heap)
    
    print(f'{-max_heap[0][0]} {min_heap[0][0]}' if min_heap else 'EMPTY')
