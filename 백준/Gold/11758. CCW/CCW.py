a,b,c=[[*map(int,input().split())] for _ in range(3)]
d=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
print((d>0)-(d<0))