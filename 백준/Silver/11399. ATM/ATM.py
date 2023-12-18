n=int(input())
a=sorted(map(int,input().split()))
print(sum([sum(a[:i]) for i in range(1,n+1)]))