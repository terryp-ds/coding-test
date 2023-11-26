x,y=map(int,input().split())
z=y*100//x
if z>=99:print(-1)
else:
    a,s,e=0,1,x
    while s<=e:
        m=(s+e)//2
        if (y+m)*100//(x+m)<=z: s=m+1
        else: a,e=m,m-1
    print(a)