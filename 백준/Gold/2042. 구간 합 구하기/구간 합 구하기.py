import sys
input = sys.stdin.readline

def init(n,s,e):
    if s==e:
        t[n]=v[s-1]
    else:
        m=(s+e)//2
        t[n]=init(n*2,s,m)+init(n*2+1,m+1,e)
    return t[n]

def query(n,s,e,l,r):
    if s>r or l>e:
        return 0
    if s>=l and r>=e:
        return t[n]
    m=(s+e)//2
    return query(n*2,s,m,l,r)+query(n*2+1,m+1,e,l,r)

def update(n,s,e,i,d):
    if s>i or i>e:
        return
    t[n]+=d
    if s!=e:
        m=(s+e)//2
        update(n*2,s,m,i,d)
        update(n*2+1,m+1,e,i,d)

n,m,k=map(int,input().split())
v=[int(input()) for _ in range(n)]
t=[0]*(1<<(n.bit_length()+1))

init(1,1,n)

for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update(1,1,n,b,c-v[b-1])
        v[b-1]=c
    else:
        print(query(1,1,n,b,c))