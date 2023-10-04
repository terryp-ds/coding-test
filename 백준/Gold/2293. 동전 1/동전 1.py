n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]
d=[0 for i in range(k+1)]
d[0]=1
for i in a:
    for j in range(i,k+1):
        if j-1>=0: d[j]+=d[j-i]
print(d[k])