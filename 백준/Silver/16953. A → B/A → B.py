a,b=map(int,input().split())
c=1
while b>a:
    if b%10==1: b//=10
    elif b%2: break
    else: b//=2
    c+=1
print([-1,c][a==b])