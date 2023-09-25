a,b = input(), input()
n,m = len(a), len(b)
dp = [['']*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + a[i-1]
        else:
            dp[i][j] = dp[i][j-1] if len(dp[i][j-1])>len(dp[i-1][j]) else dp[i-1][j]
print(len(dp[-1][-1]))
print(dp[-1][-1])