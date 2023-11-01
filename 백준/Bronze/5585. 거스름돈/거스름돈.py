n=1000-int(input())
c=0
for m in [500,100,50,10,5,1]:c,n=c+n//m,n%m
print(c)