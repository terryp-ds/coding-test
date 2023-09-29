import sys
input = sys.stdin.readline

q=10**9+7

def init(n,s,e):
    if s==e: t[n]=v[s-1]
    else:
        m=(s+e)//2
        t[n]=init(n*2,s,m)*init(n*2+1,m+1,e)%q
    return t[n]

def query(n,s,e,l,r):
    if s>r or e<l: return 1
    if s>=l and r>=e: return t[n]
    m=(s+e)//2
    return query(n*2,s,m,l,r)*query(n*2+1,m+1,e,l,r)%q

def update(n,s,e,i,z):
    if s>i or i>e: return t[n]
    if s==e: t[n]=z%q
    else:
        m=(s+e)//2
        t[n]=update(n*2,s,m,i,z)*update(n*2+1,m+1,e,i,z)%q
    return t[n]

n,m,k=map(int,input().split())
v=[int(input()) for _ in range(n)]
t=[0]*(1<<(n.bit_length()+1))

init(1,1,n)

for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1: update(1,1,n,b,c)
    else: print(query(1,1,n,b,c))