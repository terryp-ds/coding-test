import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]

min_s = 3e9
left, right = 0, n-1
ans = []

while left < right:
    s = a[left]+a[right]

    if abs(s) < min_s:
        min_s = abs(s)
        ans = [a[left],a[right]]

    if min_s == 0:
        break

    if s < 0:
        left += 1

    else:
        right -= 1

print(*ans)
