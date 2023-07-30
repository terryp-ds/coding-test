import sys

input = sys.stdin.readline

n = int(input())
m = [list(map(int, list(input().rstrip()))) for _ in range(n)]
graph = [[] for _ in range(n*n)]

for y in range(n):

    for x in range(n):

        v = m[y][x]
        c = y*n+x

        if v:
            if y > 0 and m[y-1][x]:
                graph[c].append(c-n)

            if x > 0 and m[y][x-1]:
                graph[c].append(c-1)

            if y < n-1 and m[y+1][x]:
                graph[c].append(c+n)

            if x < n-1 and m[y][x+1]:
                graph[c].append(c+1)

visited = [0]*n*n
group = []
c = 0

for i in range(n*n):
    y,x = i//n, i%n

    if m[y][x] and not visited[i]:

        stack = [i]
        group.append(0)

        while stack:
            vertex = stack.pop()

            if not visited[vertex]:
                group[c] += 1
                visited[vertex] = 1

                for v in graph[vertex]:
                    if not visited[v]:
                        stack.append(v)


        c += 1


print(len(group))
print(*sorted(group), sep='\n')
