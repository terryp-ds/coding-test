from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]

    for i in range(1,n+1):
        graph[arr[i-1]] = arr[i:]

    dim = [0]*(n+1)

    for i in range(n):
        dim[arr[i]] = i
        
    m = int(input())
    
    if m == 0:
        print(*arr, sep=' ')

    else:
        for _ in range(m):
            v1,v2 = list(map(int, input().split()))
            
            if v1 in graph[v2]:
                graph[v2].remove(v1)
                graph[v1].append(v2)
                dim[v1] -= 1
                dim[v2] += 1
                
            else:
                graph[v1].remove(v2)
                graph[v2].append(v1)
                dim[v2] -= 1
                dim[v1] += 1             
               
        queue = deque()
        
        for i in range(1,n+1):
            if dim[i] == 0:
                queue.append(i)

        sorted_arr = []
        
        while queue:
            node = queue.popleft()
            sorted_arr.append(node)    

            for next_node in graph[node]:
                dim[next_node] -= 1

                if dim[next_node] == 0:
                    queue.append(next_node)
            
        if len(sorted_arr) == n:
            print(*sorted_arr, sep=' ')

        else:
            print('IMPOSSIBLE')
