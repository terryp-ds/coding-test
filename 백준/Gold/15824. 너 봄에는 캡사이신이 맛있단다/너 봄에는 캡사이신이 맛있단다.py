n=int(input())
a=sorted([*map(int,input().split())])
print((sum([a[i]*(2**i-1) for i in range(n)])-sum([a[i]*(2**(n-1-i)-1) for i in range(n)]))%(10**9+7))