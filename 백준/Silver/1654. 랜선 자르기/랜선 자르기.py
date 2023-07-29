import sys

n, target = list(map(int, input().split()))
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    
    if sum(map(lambda x: x//mid, arr)) >= target:
        start = mid + 1
        
    else:
        end = mid - 1


print(end)
