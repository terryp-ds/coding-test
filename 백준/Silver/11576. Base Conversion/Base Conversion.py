a,b=map(int,input().split())
m=int(input())
s=sum([x*(a**(m-i-1)) for i,x in enumerate([*map(int,input().split())])])
a=[]
while s:
    a+=[s%b]
    s//=b
print(*a[::-1])