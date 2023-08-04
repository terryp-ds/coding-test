from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

cnt = 1
queue = deque([[i] for i in range(1,n+1)])

while cnt < m:

    queue2 = deque()

    while queue:
        node = queue.popleft()
        
        for i in range(node[-1], n+1):
            queue2.append(node+[i])

    queue = queue2
    cnt += 1


for arr in queue:
    print(*arr, sep=' ')
