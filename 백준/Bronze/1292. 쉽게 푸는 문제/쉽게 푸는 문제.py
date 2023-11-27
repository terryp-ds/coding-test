a,b=map(int,input().split())
s=[i for j in [[k]*k for k in range(1,46)] for i in j]
print(sum(s[:b])-sum(s[:a-1]))