for _ in range(int(input())):
 a,*b=map(int,input().split())
 m=sum(b)/a
 print(f'{sum([x>m for x in b])/a*100:.3f}%')