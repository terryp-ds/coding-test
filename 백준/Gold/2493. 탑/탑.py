n=int(input())
a=[*map(int,input().split())]
s=[(a[0],0)]
d=[0]
for i in range(1,n):
 while s and s[-1][0]<a[i]: s.pop()
 if not s: d+=[0]
 else: d+=[s[-1][1]+1]
 s+=[(a[i],i)]
print(*d)