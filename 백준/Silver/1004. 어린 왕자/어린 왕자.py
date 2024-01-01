for _ in range(int(input())):
 x,y,u,w=map(int,input().split())
 c=0
 for _ in range(int(input())):
  a,b,r=map(int,input().split())
  d1=(x-a)**2+(y-b)**2
  d2=(u-a)**2+(w-b)**2
  r**=2
  c+=(r>d1)^(r>d2)
 print(c)