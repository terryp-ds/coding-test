from collections import deque
def solution(arr):
    q = deque(arr)
    a = [-1]
    while q:
        n = q.popleft()
        if a[-1] != n:
            a.append(n)
    return a[1:]