n,m=map(int,input().split())
print(sorted([input() for _ in range(n)])[m-1])