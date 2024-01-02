n=int(input())
a=[[' ']*(2*n-1) for _ in range(n)]
def star(s,c,e):
 if e-s==2:
  a[s][c]='*'
  a[s+1][c-1]='*'
  a[s+1][c+1]='*'
  a[s+2][c-2:c+3]=['*']*5
 else:
  m,d=(s+e)//2,(e-s)//2
  for t in [(s,c,m),(m+1,c-d-1,e),(m+1,c+d+1,e)]:star(*t)
star(0,n-1,n-1)
for i in a: print(*i,sep='')