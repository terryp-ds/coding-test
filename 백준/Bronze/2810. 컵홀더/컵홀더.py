n=int(input())
print(min(n,n+1-input().count('L')//2))