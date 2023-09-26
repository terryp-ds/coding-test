import bisect as b

n=int(input())
s=[*map(int,input().split())]
a=[0]*n
c=[]

for i in range(n):
    if not c or s[i]>c[-1]:
        c.append(s[i])
        a[i]=len(c)-1
    else:
        a[i]=b.bisect_left(c,s[i])
        c[a[i]]=s[i]
print(len(c))

m,l=max(a)+1,[]
for i in range(n-1,-1,-1):
    if a[i]==m-1:
        l.append(s[i])
        m=a[i]
print(*l[::-1])