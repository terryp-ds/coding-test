for _ in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    n=((a-d)**2+(b-e)**2)**0.5
    if not n and c==f:
        print(-1)
    elif n==abs(c-f) or n==c+f:
        print(1)
    elif abs(c-f)<n<c+f:
        print(2)
    else:
        print(0)