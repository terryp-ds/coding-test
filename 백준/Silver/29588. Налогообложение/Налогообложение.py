x,k=map(int,input().split())
u=[0]+[*map(int,input().split())]
t=[*map(int,input().split())]
a,i=0,0
for i in range(k):
 m=min(x,u[i+1]-u[i])
 a+=m*t[i]/100
 x-=m
 if x<=0:break
if x>0:a+=x*t[k]/100
print(f'{round(a,2):.2f}')