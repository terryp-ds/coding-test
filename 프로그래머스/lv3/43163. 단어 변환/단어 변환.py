from collections import deque

def solution(begin, target, words):
    words.append(begin)
    graph = {i:[] for i in words}
    visited = {i:0 for i in words+[target]}
    n = len(words)
    m = len(begin)
    
    for i in range(n):
        for j in range(i,n):
            if sum([x==y for x,y, in zip(words[i], words[j])]) == m-1:
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    
    queue = deque([begin])
    visited[begin] = 1
    
    while queue:
        node = queue.popleft()
        
        if node == target:
            return visited[target]-1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = visited[node] + 1
        

    return 0