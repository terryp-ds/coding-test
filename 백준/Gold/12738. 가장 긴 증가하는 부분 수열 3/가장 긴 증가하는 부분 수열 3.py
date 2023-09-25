import bisect as b
n=int(input())
a=list(map(int,input().split()))
l=[a[0]]
for i in range(1,n):
    if a[i]>l[-1]:l.append(a[i])
    else:l[b.bisect_left(l,a[i])]=a[i]
print(len(l))