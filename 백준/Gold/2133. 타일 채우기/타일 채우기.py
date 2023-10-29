n=int(input())
d=[0]*30
d[1]=3
for i in range(3,n,2): d[i]=d[i-2]*3+sum(d[:i-2])*2+2
print(d[n-1])