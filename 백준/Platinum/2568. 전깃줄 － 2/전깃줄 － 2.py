import bisect as b
d={v:k for k,v in sorted([[*map(int,input().split())] for _ in range(int(input()))], key=lambda x:x[0])}
s=list(d.keys())
n=len(s)
a=[0]*n
c=[]

for i in range(n):
    if not c or s[i]>c[-1]:
        c.append(s[i])
        a[i]=len(c)-1
    else:
        a[i]=b.bisect_left(c,s[i])
        c[a[i]]=s[i]
print(n-len(c))

m,l=max(a)+1,[]
for i in range(n-1,-1,-1):
    if a[i]==m-1:
        l.append(s[i])
        m=a[i]
print(*sorted([d[i] for i in set(s)-set(l)]),sep='\n')