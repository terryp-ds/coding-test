import sys
input = sys.stdin.readline

def init(n,s,e):
    if s==e:
        t[n]=a[s-1]
    else:
        m=(s+e)//2
        t[n]=min(init(n*2,s,m),init(n*2+1,m+1,e))
    return t[n]

def query(n,s,e,l,r):
    if s>r or e<l:
        return 2e9
    if s>=l and r>=e:
        return t[n]
    m=(s+e)//2
    return min(query(n*2,s,m,l,r),query(n*2+1,m+1,e,l,r))

def update(n,s,e,i,j):
    if s>i or i>e: return
    if s==e:
        a[s-1],t[n]=j,j
        return t[n]
    m=(s+e)//2
    update(n*2,s,m,i,j)
    update(n*2+1,m+1,e,i,j)
    t[n]=min(t[n*2],t[n*2+1])

n=int(input())
a=[*map(int,input().split())]
t=[0]*(1<<(n.bit_length()+1))

init(1,1,n)

for _ in range(int(input())):
    c,i,j=map(int, input().split())
    if c==1: update(1,1,n,i,j)        
    else: print(query(1,1,n,i,j))