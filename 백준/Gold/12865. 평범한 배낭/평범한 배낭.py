import sys

n,k = map(int, input().split())
arr = []

for _ in range(n):
    w,v = map(int, input().split())
    arr.append([w,v])

arr = sorted(arr)
w,v = [x[0] for x in arr], [x[1] for x in arr]

def dp(n, k, w, v):
    arr = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,k+1):
            if w[i-1] <= j:
                arr[i][j] = max(v[i-1]+arr[i-1][j-w[i-1]], arr[i-1][j])

            else:
                arr[i][j] = arr[i-1][j]

    return arr[n][k]

print(dp(n,k,w,v))
