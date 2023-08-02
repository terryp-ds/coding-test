from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = list(map(int, input().split()))
s = sum(arr[:k])
max_sum = s
arr1, arr2 = deque(arr[:k]), deque(arr[k:])

while arr2:
    a,b = arr1.popleft(), arr2.popleft()
    arr1.append(b)
    s += b-a
    if s > max_sum:
        max_sum = s

print(max_sum)
