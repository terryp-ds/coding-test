from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m,w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.extend([[e,s,t] for s,e,t in edges[:m]])
    edges.extend([[s,e,-t] for s,e,t in [list(map(int, input().split())) for _ in range(w)]])

    for s,e,t in edges:
        graph[s].append((t,e))

    dist = [10001 for _ in range(n+1)]
    pred = [None for _ in range(n+1)]
    dist[edges[0][0]] = 0

    for _ in range(1,n+1):
        for s,e,t in edges:
            if dist[s] + t < dist[e]:
                dist[e] = dist[s] + t
                pred[e] = s

    flag = 0

    for s,e,t in edges:
        if dist[s] + t < dist[e]:
            flag = 1
            break

    print('YES' if flag else 'NO')
