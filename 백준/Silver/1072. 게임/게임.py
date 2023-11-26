x,y=map(int,input().split())
z=y*100//x
n=z*x+x-y*100
d=99-z
print(-1 if z>98 else n//d+(n%d>0))