a,b=map(int,input().split())
m=int(input())
s=sum([x*(a**(m-i-1)) for i,x in enumerate([*map(int,input().split())])])
n=0
while b**n<s: n+=1
a=[]
for i in range(n):
    q=b**(n-1-i)
    p,s=s//q,s%q
    a+=[p]
print(*a)