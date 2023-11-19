n=int(input())
a=[[' ']*(2*n-1) for _ in range(n)]
def star(s,m,e):
    if e-s==2:
        a[s][m]='*'
        a[s+1][m-1]='*'
        a[s+1][m+1]='*'
        a[s+2][m-2:m+3]=['*']*5
    else:
        star(s,m,(s+e)//2)
        star((s+e)//2+1,m-(e-s)//2-1,e)
        star((s+e)//2+1,m+(e-s)//2+1,e)
star(0,n-1,n-1)
for i in a:print(*i,sep='')