import sys
input = sys.stdin.readline
    
n = int(input())

max_dp = [0]*3
min_dp = [0]*3

for i in range(n):
    arr = list(map(int, input().split()))
    max_dp = [max(max_dp[:2])+arr[0], max(max_dp)+arr[1], max(max_dp[1:])+arr[2]]
    min_dp = [min(min_dp[:2])+arr[0], min(min_dp)+arr[1], min(min_dp[1:])+arr[2]]

print(max(max_dp), min(min_dp))
