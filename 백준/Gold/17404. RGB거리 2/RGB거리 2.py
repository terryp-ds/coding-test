import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 10**7

for i in range(3):
    dp = [[10**7]*3 for _ in range(n)]
    dp[0][i] = a[0][i]

    for j in range(1,n):
        for k in range(3):
            dp[j][k] = a[j][k] + min(dp[j-1][(k+1)%3], dp[j-1][(k+2)%3])

    for j in range(1,3):
        ans = min(ans, dp[-1][(i+j)%3])

print(ans)