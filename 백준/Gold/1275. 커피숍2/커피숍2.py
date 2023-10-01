import sys
input=sys.stdin.readline

def init(k,s,e):
    if s==e: t[k]=v[s-1]
    else:
        m=(s+e)//2
        t[k]=init(k*2,s,m)+init(k*2+1,m+1,e)
    return t[k]

def query(k,s,e,l,r):
    if s>r or l>e: return 0
    if s>=l and r>=e: return t[k]
    m=(s+e)//2
    return query(k*2,s,m,l,r)+query(k*2+1,m+1,e,l,r)

def update(k,s,e,i,d):
    if s>i or i>e: return
    t[k]+=d
    if s!=e:
        m=(s+e)//2
        update(k*2,s,m,i,d)
        update(k*2+1,m+1,e,i,d)

n,q=map(int,input().split())
v=[*map(int,input().split())]
t=[0]*(1<<(n.bit_length()+1))

init(1,1,n)

for _ in range(q):
    x,y,a,b=map(int,input().split())
    if x>y:x,y=y,x
    print(query(1,1,n,x,y))
    update(1,1,n,a,b-v[a-1])
    v[a-1]=b