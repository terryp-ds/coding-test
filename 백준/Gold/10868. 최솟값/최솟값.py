import sys
input = sys.stdin.readline

def init(s,e,n):
    if s==e:
        t[n]=a[s]
    else:
        m=(s+e)//2
        t[n]=min(init(s,m,n*2),init(m+1,e,n*2+1))
    return t[n]

def query(n,s,e,l,r):
    if s>r or e<l:
        return 2e9
    if s>=l and r>=e:
        return t[n]
    m=(s+e)//2
    return min(query(n*2,s,m,l,r), query(n*2+1,m+1,e,l,r))

n,m=map(int, input().split())
a=[int(input()) for _ in range(n)]
t=[0]*(1<<(n.bit_length()+1))

init(0,n-1,1)

for _ in range(m):
    i,j=map(int, input().split())
    print(query(1,0,n-1,i-1,j-1))