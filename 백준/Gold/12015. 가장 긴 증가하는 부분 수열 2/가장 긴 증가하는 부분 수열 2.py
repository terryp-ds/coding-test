import sys
input = sys.stdin.readline

_=input()
arr=[0]+[*map(int,input().split())]
lis = [0]

for i in arr:
    if lis[-1]<i: lis.append(i)
    else:
        l,r = 0,len(lis)       
        while l<r:
            m=(l+r)//2
            if lis[m]<i: l=m+1
            else: r=m
        lis[r]=i

print(len(lis)-1)