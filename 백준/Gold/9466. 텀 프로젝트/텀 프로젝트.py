import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    graph = [*map(int, input().split())]
    visited = [0]*(n+1)
    m = 0

    for i in range(1,n+1):
        if not visited[i]:
            stack = [i]
            group = [i]
            c = 1

            while stack:
                s = stack.pop()
                e = graph[s-1]

                if s == e:
                    visited[e] = 1
                    m += 1
                    break

                elif i == e:
                    visited[e] = 1
                    m += c
                    break

                elif not visited[e]:
                    visited[s] = 1
                    c += 1
                    stack.append(e)
                    group.append(e)

                elif visited[e] and e in group:
                    m += c - group.index(e)
                    visited[e] = 1
                    break
    print(n-m)