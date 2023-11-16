x=int(input())
i=1
while i<x: x-=i; i+=1
a,b=i-x+1,x
print(f'{a}/{b}' if i%2 else f'{b}/{a}')