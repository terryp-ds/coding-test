n=int(input())
a=[*map(int,input().split())]
t=int(input())
a.sort()
i,j,c=0,n-1,0
while i<j:
    s=a[i]+a[j]
    if s==t: c+=1; i+=1
    elif s<t: i+=1
    else: j-=1
print(c)