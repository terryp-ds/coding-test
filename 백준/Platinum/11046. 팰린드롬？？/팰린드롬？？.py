import sys
input=sys.stdin.readline
input()
a=input().strip().split()
b=[-1]*(len(a)*2+1)
b[1::2] = a
m=len(b)
p=[0]*m
r,c=-1,-1
for i in range(m-1):
    if r>=i:
        p[i]=min(r-i, p[c*2-i])
    while i+p[i]+1<m and b[i+p[i]+1] == b[i-p[i]-1]:
        p[i]+=1
    if i+p[i]>r:
        r=i+p[i]
        c=i
for _ in range(int(input())):
    e,f = map(int,input().split())
    print(0+(f-e<=p[e+f-1]))