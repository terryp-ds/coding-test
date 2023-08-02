import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(arr))
    
else:
    dp = [0]*n

    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]

    for i in range(2, n):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

    print(dp[i])
