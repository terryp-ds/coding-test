n,m = map(int, input().split())
arr = sorted(set(map(int, input().split())), reverse=True)

stack = [[i] for i in arr]

while stack:
    num = stack.pop()
    
    if len(num) == m:
        print(*num)
        continue
    
    for i in arr:
        if i >= num[-1]:
            stack.append(num+[i])
