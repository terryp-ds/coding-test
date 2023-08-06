n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []

def dfs():
    if len(stack) == m:
        print(*stack)
        return None

    else:
        for i in range(n):
            if not stack or stack[-1] <= arr[i]:
                stack.append(arr[i])
                dfs()
                stack.pop()

dfs()
