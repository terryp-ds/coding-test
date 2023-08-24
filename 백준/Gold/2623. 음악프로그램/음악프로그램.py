from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dim = [0]*(n+1)

for _ in range(m):
    a = list(map(int, input().split()))

    for i in range(len(a)-2):
        graph[a[i+1]].append(a[i+2])
        dim[a[i+2]] += 1

queue = deque([])

for i in range(n):
    if not dim[i+1]:
        queue.append(i+1)

arr = []

while queue:
    v = queue.popleft()
    arr.append(v)

    for e in graph[v]:
        dim[e] -= 1
        if not dim[e]:
            queue.append(e)

if len(arr) != n:
    print(0)

else:
    print(*arr, sep='\n')