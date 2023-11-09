n=int(input())
a=[list(' '*n) for _ in range(n)]
def star(x1,y1,x2,y2):
    if x2-x1==3 and y2-y1==3:
        for y in range(y1,y2):
            a[y][x1:x2]='*'*3
        a[y1+1][x1+1]=' '
        return
    for i in range(3):
        for j in range(3):
            if i==j==1: continue
            x,y=(x2-x1)//3,(y2-y1)//3
            star(x1+x*i,y1+y*j,x1+x*(i+1),y1+y*(j+1))
star(0,0,n,n)
for i in a: print(*i,sep='')