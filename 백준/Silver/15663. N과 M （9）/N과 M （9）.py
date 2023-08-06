n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []
prev = 0
visited = [0]*n

def dfs():
    prev = 0
    
    if len(stack) == m and prev != stack:
        print(*stack)
        return None

    else:
        for i in range(n):
            num = arr[i]
            
            if num != prev and not visited[i]:
                stack.append(num)
                prev = num
                visited[i] = 1
                dfs()
                stack.pop()
                visited[i] = 0

dfs()
