def solution(n, computers):
    
    graph = [[] for _ in range(n)]

    for k in range(n):
        for i, j in enumerate(computers[k]):
            if j and i != k:
                graph[k].append(i)

    visited = [0]*n
    cnt = 0

    for i in range(n):
        stack = [i]

        if not visited[i]:
            cnt += 1

            while stack:
                cur = stack.pop()

                if not visited[cur]:
                    visited[cur] = 1

                    for nex in graph[cur]:
                        if not visited[nex]:
                            stack.append(nex)

    return cnt