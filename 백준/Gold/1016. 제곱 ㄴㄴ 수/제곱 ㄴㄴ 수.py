n,m=map(int,input().split())
a=[1]*(m-n+1)
for i in range(2,int(m**.5)+1):
    k=i**2
    for j in range(n//k*k,m+1,k):
        if j-n>=0 and a[j-n]: a[j-n]=0
print(sum(a))