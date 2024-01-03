n,r,c=map(int,input().split())
s=0
while n>0:
 h=2**(n-1)
 y,x=(r>=h),(c>=h)
 s+=(y*2+x)*(h**2)
 r-=h*y
 c-=h*x
 n-=1
print(s+r*2+c)