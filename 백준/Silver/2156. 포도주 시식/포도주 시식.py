import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(arr))

else:
    dp = [0]*10000
    
    dp[0], dp[1], dp[2] = arr[0], arr[0]+arr[1], max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2])

    for i in range(3, n):
        dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])

    print(dp[n-1])
