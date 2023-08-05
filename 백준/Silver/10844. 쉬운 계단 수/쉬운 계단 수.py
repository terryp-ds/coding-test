n = int(input())

dp = [0]+[1]*9

for _ in range(1,n):
    dp = [dp[1]] + [dp[i-1]+dp[i+1] for i in range(1,9)] + [dp[8]]
    dp = list(map(lambda x: x % 10**9, dp))
    
print(sum(dp) % 10**9)
