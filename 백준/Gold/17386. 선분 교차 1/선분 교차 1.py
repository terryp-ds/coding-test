def ccw(a,b,c):
    return ((b[0]-a[0]) * (c[1]-a[1]) - (b[1]-a[1]) * (c[0]-a[0]))

x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
a,b=(x1,y1),(x2,y2)
c,d=(x3,y3),(x4,y4)
print(int((ccw(a,b,c)*ccw(a,b,d)<0)&(ccw(c,d,a)*ccw(c,d,b)<0)))
