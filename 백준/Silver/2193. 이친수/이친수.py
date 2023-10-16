n=int(input())
a=[0]*(n+1)
a[1]=[0,1]
for i in range(2,n+1): a[i]=[sum(a[i-1]),a[i-1][0]]
print(sum(a[n]))