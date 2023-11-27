n,m=map(int,input().split())
a=[int(input()) for _ in range(int(input()))]
l,r,c=1,m,0
for i in a:
    if i<l: l,r,c=i,i+m-1,c+l-i
    if i>r: l,r,c=i-m+1,i,c+i-r
print(c)