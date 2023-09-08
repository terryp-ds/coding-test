import sys
input = sys.stdin.readline

def init(t,n,s,e,f):
    if s==e:
        t[n]=a[s]
    else:
        m=(s+e)//2
        if f:
            t[n]=max(init(t,n*2,s,m,f),init(t,n*2+1,m+1,e,f))
        else:
            t[n]=min(init(t,n*2,s,m,f),init(t,n*2+1,m+1,e,f))
    return t[n]

def query(t,n,s,e,l,r,f):
    if s>r or e<l:
        return 0 if f else 2e9
    if s>=l and r>=e:
        return t[n]
    m=(s+e)//2
    return max(query(t,n*2,s,m,l,r,f), query(t,n*2+1,m+1,e,l,r,f)) if f else min(query(t,n*2,s,m,l,r,f), query(t,n*2+1,m+1,e,l,r,f))

n,m=map(int,input().split())
a=[int(input()) for _ in range(n)]
t1=[0]*(1<<(n.bit_length()+1))
t2=t1.copy()

init(t1,1,0,n-1,0)
init(t2,1,0,n-1,1)

for _ in range(m):
    i,j=map(int,input().split())
    print(query(t1,1,0,n-1,i-1,j-1,0),query(t2,1,0,n-1,i-1,j-1,1))