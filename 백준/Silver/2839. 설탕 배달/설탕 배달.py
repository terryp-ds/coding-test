n=int(input())
if n%5==0:
    print(n//5)
else:
    m=n//5
    f=1
    while m>=0:
        if (n-m*5)%3==0:
            f=0
            print(m+(n-m*5)//3)
            break
        else:
            m-=1
    if f:
        print(-1)