import sys
input=sys.stdin.readline

def cut(h):
    l=0
    for i in range(n):
        if a[i]<h: break
        else: l+=a[i]-h
    return l

n,t=map(int,input().split())
a=sorted(map(int,input().split()),reverse=True)
s,e=1,a[0]

while s<=e:
    m=(s+e)//2
    c=cut(m)
    if c<t: e=m-1
    else: s=m+1

print(e)