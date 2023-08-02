from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    visited = {}
    a,b = map(int, input().split())
    queue = deque([(a, '')])

    while queue:
        node, cmd = queue.popleft()

        if node == b:
            break

        if node not in visited:
            visited[node] = 0

            queue.append((2*node % 10000, cmd+'D'))
            queue.append(((node+9999) % 10000, cmd+'S'))
            tmp = str(node).zfill(4)
            queue.append((int(tmp[1:]+tmp[0]), cmd+'L'))
            queue.append((int(tmp[-1]+tmp[:-1]), cmd+'R'))
 

    print(cmd)
